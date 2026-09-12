import json
from datetime import datetime
def load_expense():
     with open('expense.json','r') as fp:
          return json.load(fp)

def save_expense(expenses):
     with open('expense.json','w') as fp:
          json.dump(expenses,fp,indent=4)
          
def add_expense():
     print(f"==========================Add Expense==========================")
     while True:
          try:
            amount = int(input("Enter the amount :"))
            if amount <= 0:
                 print("Amount must be greater than 0 ")
                 continue
            break
          except ValueError:
            print("Please Enter the valid number")
     while True:
       category = input("Enter the category: ").strip()
       if category == "":
            print("Category Can Not be empty") 
            continue
       break 
         
     while True:
          description = input("Enter the description: ").strip()
          if description == "":
               print("Description Cannot be empty")
               continue
          break
     while True:
          try:
               dd_mm_yyyy = input("Enter the DD-MM-YYYY: ")
               datetime.strptime(dd_mm_yyyy,"%d-%m-%Y")
               break
          except ValueError:
               print("Please Enter a valid date")            
     d = load_expense()
     if d:
          id = max(expense['id'] for expense in d) + 1
     else:
         id = 1
     expense_data = {
         "id" : id,
         "amount" : amount,
         "category":category,
         "description":description,
         "dd_mm_yyyy" : dd_mm_yyyy
     }
     d.append(expense_data)
     save_expense(d)

def view_expense():
        d = load_expense()
        print("=========================ALL EXPENSES=======================")
        print()
        print(f"{'ID':<3} | {'Amount':<8} | {'Category':<12} | {'Description':<15} | {'Date':<12}")
        print("-" * 60)
    
        for data in d:
          print(f"{data['id']:<3} | ₹{data['amount']:<7} | {data['category']:<12} | {data['description']:<15} | {data['dd_mm_yyyy']:<12}")
    
        print("-" * 60)

def search_expense():
       print("============================Search Expense==============================\n")
      
       while True:
            try:
                id = int(input("Enter id :"))
                if id <= 0:
                    print("Id should be greater than 0")
                    continue
                break
            except ValueError:
                print("Invalid Id")         
       d = load_expense()
       found = False
       for data in d:
          if data['id'] == id:
                print(f"""
ID : {data['id']}
Amount : {data['amount']}
Category : {data['category']}
Description : {data['description']}
Date : {data['dd_mm_yyyy']}
""")
                found = True
                break
       if not found:
             print("Expense Not Found")

def edit_expense():
     print("================================Edit Expense=============================")
     while True:
          try:
               id = int(input("Enter a expense id:"))
               if id <= 0:
                    print("ID must be greater than 0")
                    continue
               break
          except ValueError:
               print("Invalid ID")
     found = False
     cancel = False
     d = load_expense()
     for data in d:
        if data['id'] == id:
            print(f"{data['id']:<3} | ₹{data['amount']} | {data['category']:<12} | {data['description']:<15} | {data['dd_mm_yyyy']:<12} ")
            print("What Do You Want To Edit ?")
            print("""
    1.Amount
    2.Category
    3.Description
    4.Date
    5.Cancel
    """)
            while True:
                 
               try:
                     choice = int(input("Enter your choice :"))
                     if choice < 1 or choice > 5:
                         print("Please Enter the valid choice")
                         continue
                     break
               except ValueError:
                    print("Please Enter a number")
            match choice:
                    case 1:
                        while True:
                            try:
                              amount = int(input("Enter a amount :"))
                              if amount <= 0 :
                                   print("Enter amount greater than 0")
                                   continue
                              break
                            except ValueError:
                                 print("Enter the valid number")     
                        data['amount'] = amount
                        found = True
                        break
                    case 2:
                        while True:
                             category = input("Enter the Category:").strip()
                             if category == "":
                                  print("Category is empty Please enter")
                                  continue
                             break
                        data['category'] = category
                        found = True
                        break
                    case 3:
                        while True:
                             description = input("Enter the Description:").strip()
                             if description == "":
                                  print("Description is empty Please enter")
                                  continue
                             break
                        data['description'] = description
                        found = True
                        break
                    case 4:
                        while True:
                             try:
                                  dd_mm_yyyy = input("Enter the DD-MM-YYYY :")
                                  datetime.strptime(dd_mm_yyyy,"%d-%m-%Y")
                                  break
                             except ValueError:
                                print("Please Enter the valid date")
                        data['dd_mm_yyyy'] = dd_mm_yyyy
                        found = True
                        break
                    case 5:
                        cancel = True
                        break
     if found :
            save_expense(d)
            print("Expense Update Successfully")
     elif cancel:
            print("cancel edit")
     else :
          print("Expense not Found")

def delete_expense():
     print("===============================Delete Expense=======================")
     while True:
          try:
               id = int(input("Enter a id :"))
               if id <= 0:
                    print("ID must be greater than 0")
                    continue
               break
          except ValueError:
               print("ID must be a number")
     found = False
     d = load_expense()
     for data in d:
        if data["id"] == id:
            d.remove(data)
            found = True
            break
     if found:
        save_expense(d)
        print("Delete Expenses Successfully")
     else:
        print("Expense id is not exist")
def total_expense():
    print("=================================")
    print("        Total Expense            ")
    print("=================================")
    d = load_expense()
    total = 0
    for data in d:
        total += data['amount']
    print("\nTotal Expense :",total,"\n")
    print("=================================")
def category_expense():
    print("=======================Category Summary======================\n")
    category_total = {}
    d = load_expense()
    for data in d:
        if data['category'] not in category_total:
            category_total[data['category']] = data['amount']
        else:
            category_total[data['category']] += data['amount']
    print("Category            Total Expense")
    print("------------------------------------------------\n")
    for key , value in category_total.items():
        print(f"{key:<20}  ₹{value:,}")
    print("------------------------------------------------\n")
    total = 0
    for key,value in category_total.items():
        total += value
    print(f"Total Expenses :₹{total:,}")
    print("\n=================================================")
    
def monthly_expense():
    print("====================Monthly Summary======================\n")
    months = {}
    d = load_expense()
    for expense in d:
        date_time = datetime.strptime(expense['dd_mm_yyyy'],"%d-%m-%Y")
        month_year = date_time.strftime("%B %Y")
        if month_year not in months:
            months[month_year] = expense["amount"]
        else:
            months[month_year] += expense["amount"]
    for key,value in months.items():
        print(f"{key:<20} : ₹{value:,}")

def main():
        while(True):
             try: 
                choice = int(input("""
1. Add Expense\n2. View All Expense\n3. Search Expense\n4. Edit Expense\n5. Delete Expense\n6. Total Expense\n7. Category Summary\n8. Monthly Summary\n9. Exit
Enter Your Choice : """ ))
             except ValueError:
                print("Please Enter a number ")
                continue                  
             if choice < 1 or choice > 9:
                  print("Invalid Choice")
                  continue
             match choice:
                  case 1:
                       add_expense()
                  case 2:
                       view_expense()
                  case 3:
                       search_expense()
                  case 4:
                       edit_expense()
                  case 5:
                       delete_expense()
                  case 6:
                       total_expense()
                  case 7:
                       category_expense()
                  case 8:
                       monthly_expense()
                  case 9:
                       print("Thankyou For Using My Expense Tracker!")
                       break

main()
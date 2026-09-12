import json
from datetime import datetime
with open('expense.json','r') as fp:
    d = json.load(fp)

print("""
==========================================================
                   EXPENSE TRACKER
==========================================================
""",end = "")
while(True):
    choice = int(input("""
1. Add Expense\n2. View All Expense\n3. Search Expense\n4. Edit Expense\n5. Delete Expense\n6. Total Expense\n7. Category Summary\n8. Monthly Summary\n9. Exit
Enter Your Choice : """ ))

    match choice:
        case 1:
            print(f"==========================Add Expense==========================")
            amount = int(input("Enter the amount:"))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            dd_mm_yyyy = input("Enter the DD-MM-YYYY: ")
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
            with open('expense.json','w') as fp:
                json.dump(d,fp,indent=4)
        case 2:
            print("=========================ALL EXPENSES=======================")
            print()
            print(f"{'ID':<3} | {'Amount':<8} | {'Category':<12} | {'Description':<15} | {'Date':<12}")
            print("-" * 60)

            for data in d:
                print(f"{data['id']:<3} | ₹{data['amount']:<7} | {data['category']:<12} | {data['description']:<15} | {data['dd_mm_yyyy']:<12}")

            print("-" * 60)
        case 3:
            print("============================Search Expense==============================\n")
            id = int(input("Enter id :"))
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
        
        case 4:
            print("================================Edit Expense=============================")
            id = int(input("Enter a expense id:"))
            found = False
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
                    choice = int(input("Enter your choice :"))
                    match choice:
                        case 1:
                            amount = int(input("Enter a amount :"))
                            data['amount'] = amount
                            found = True
                            break
                        case 2:
                            category = input("Enter the Category:")
                            data['category'] = category
                            found = True
                            break
                        case 3:
                            description = input("Enter the Description:")
                            data['description'] = description
                            found = True
                            break
                        case 4:
                            dd_mm_yyyy = input("Enter the DD-MM-YYYY :")
                            data['dd_mm_yyyy'] = dd_mm_yyyy
                            found = True
                            break
                        case 5:
                            print("Expense Not Found")
                            break
            if found:
                 with open('expense.json','w') as fp:
                        json.dump(d,fp,indent=4)
                 print("Expense Update Successfully")
            else:
                print("Expense Not Found")


        case 5:
            print("===============================Delete Expense=======================")
            id = int(input("Enter a id :"))
            found = False
            for data in d:
                if data["id"] == id:
                    d.remove(data)
                    found = True
                    break
            if found:
                with open("expense.json" , 'w') as fp:
                    json.dump(d,fp,indent=4)
                print("Delete Expenses Successfully")
            else:
                print("Expense id is not exist")

        case 6:
            print("=================================")
            print("        Total Expense            ")
            print("=================================")
            total = 0
            for data in d:
                total += data['amount']
            print("\nTotal Expense :",total,"\n")
            print("=================================")
        case 7:
            print("=======================Category Summary======================\n")
            category_total = {}
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

        case 8:
            print("====================Monthly Summary======================\n")
            months = {}
            for expense in d:
                date_time = datetime.strptime(expense['dd_mm_yyyy'],"%d-%m-%Y")
                month_year = date_time.strftime("%B %Y")
                if month_year not in months:
                    months[month_year] = expense["amount"]
                else:
                    months[month_year] += expense["amount"]
            for key,value in months.items():
                print(f"{key:<20} : ₹{value:,}")
        case 9:
            print("Thankyou For Using My Expense Tracker!")
            break


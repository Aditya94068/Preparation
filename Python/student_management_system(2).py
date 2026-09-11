import json

with open('student_json','r') as fp:
    d = json.load(fp)

   
def add_detail():
     print("----------------Fill data-----------------")
     name = input("Enter a name:")
     age = int(input("Enter a age:"))
     college = input("Enter a college :")
     CGPA = float(input("Enter a CGPA:"))

     if d:
         roll_no = max(student['roll_no'] for student in d) + 1
     else:
         roll_no = 101
     data = {
         "roll_no" : roll_no,
         "name" : name,
         "age" : age,
         "college" : college,
         "cgpa" : CGPA,
     }
    #  duplicate = False
    #  for student in d:
    #     if student['roll_no'] == data['roll_no']:
    #          duplicate = True
    #          break
    #  if duplicate:
    #      print("Duplicate entries is not allowed")
    #  else:
     d.append(data)
     with open('student_json','w') as fp:
        json.dump(d,fp,indent=4)
     print("Student Add Succcessfully")
         
def search_student():
    print("-------------------------Search Student--------------------------")
    roll_no = int(input("Enter a roll No : "))
    found = False
    for student in d:
        if student['roll_no'] == roll_no:
            print(f"""{student['roll_no']} | {student['name']} | {student['age']} | {student['college']} | {student['cgpa']} """)
            found = True
            break
    if found == False:
        print("Student not Found")

def view_all():

    print("--------------------------------------All Student---------------------------------")
    if not d:
        print("No Student Available")
    else:
        for student in d:
            print(f"""{student['roll_no']} | {student['name']} | {student['age']} | {student['college']} | {student['cgpa']} """)
def delete_student():
    print("-------------------------------------delete Student--------------------------------")
    roll_no = int(input("Enter the roll :"))
    found = False

    for student in d:
        if student['roll_no'] == roll_no:
            d.remove(student)
            found = True
            break
    if found == True:
        with open("student_json",'w') as fp:
            json.dump(d,fp,indent=4)
        print("Student Deleted Successfully")
    else:
        print("Student Not Found for deleting")
def edit_student():
    print("-------------------------------------Edit Student---------------------------------")
    roll_no = int(input("Enter the roll no :"))
    student_found = False
    field_found = False

    for student in d:
        if student["roll_no"] == roll_no:
            student_found = True
            field = input("Enter the field:")
            if "name" == field.lower():
                name = input("Enter a name :")
                student['name']  = name
                field_found = True
                break
            elif "age" == field.lower():
                age = int(input("Enter the age:"))
                student['age'] = age
                field_found = True
                break
            elif "college" == field.lower():
                college = input("Enter the college :")
                student['college'] = college
                field_found = True
                break
            elif "cgpa" == field.lower():
                cgpa = float(input("Enter the CGPA:"))
                student['cgpa'] = cgpa
                field_found = True
                break
            break
    if student_found and field_found:
        with open('student_json' , 'w') as fp:
            json.dump(d,fp,indent=4)
        print("Student edit successfully")
    elif student_found == True and field_found == False:
        print("Student Present but field is not present")
    else:
        print("Student Not present")
while(True):

    choice = int(input("""
        Enter Your Choice
        1.Add Student
        2.Search Student
        3.View All
        4.Delete Student
        5.Edit Student
        6.Exit
"""))
    match choice:
        case 1:
            add_detail()
        case 2:
            search_student()
        case 3:
            view_all()
        case 4:
            delete_student()
        case 5:
            edit_student()
        case 6:
            print("---------------Exit-----------------")
            break
        
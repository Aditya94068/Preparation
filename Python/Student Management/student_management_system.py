import json


with open("student_json",'r') as fp:
    d = json.load(fp)

while True :
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
            print("Fill data")
            name = str(input("Enter a name:"))
            age = int(input("Enter a age:"))
            college = str(input("Enter a college :"))
            CGPA = float(input("Enter a CGPA:"))
            enrolled = False

            if d:
                roll_no = max(student["roll_no"] for student in d) + 1
            else:
                roll_no = 101

            data = {
            "roll_no" : roll_no,
            "name" : name,
            "age": age,
            "college" : college,
            "cgpa" : CGPA,
            "enrolled" : True
            }
            duplicate = False
            for student in d:
                if student["roll_no"] == data["roll_no"]:
                    duplicate = True
                    break
            if duplicate:
                print("Student is Already In the data")
            else:
                d.append(data)
                with open("student_json",'w') as fp:
                    json.dump(d,fp,indent=4)
                print("Student Added Successfully")


        case 2:
            print("Search Student Data")
            r_no = int(input("Enter the roll no :"))
            found = False
            for student in d :
                if student['roll_no'] == r_no:
                   print(f"""{student['roll_no']} | {student['name']} | {student['age']} | {student['college']} | {student['cgpa']} | {student['enrolled']} """)
                   found = True
                   break
            if found == False:
                print("Student is not Present")              
        case 3:
            print("ALL student")
            for student in d:
                print(f"""{student['roll_no']} | {student['name']} | {student['age']} | {student['college']} | {student['cgpa']} | {student['enrolled']} """)
        case 4:
            print("Delete Student ")
            r_no = int(input("Enter a roll no :"))
            found = False
            for student in d:
                if student['roll_no'] == r_no:
                    d.remove(student)
                    found = True
                    break
            if found == True:
                with open('student_json','w') as fp:
                    json.dump(d,fp,indent=4)
                print("Student data deleted Successfully")
            else:
                print("Student Not Found")

        case 5:
            print("Edit Student")
            r_no = int(input("Enter the roll No :"))
            student_found = False
            field_found = False
            for student in d:
                if student["roll_no"] == r_no:
                    student_found = True
                    field = input("""Enter the Section Which You want to edit :""")
                    if "name" == field.lower():
                        name = input("Enter a name :")
                        student['name'] = name
                        field_found = True
                        break
                    elif "age" == field.lower():
                        age = int(input("Enter the age :"))
                        student['age'] = age
                        field_found = True
                        break
                    elif "cgpa" == field.lower():
                        cgpa = float(input("Enter the cgpa :"))
                        student['cgpa'] = cgpa
                        field_found = True
                        break
                    elif "college" == field.lower():
                        college = input("Enter a the college :")
                        student['college'] = college
                        field_found = True
                        break
                    break
            if student_found and field_found:
                with open('student_json','w') as fp:
                    json.dump(d,fp,indent=4)
                print("Edit Successfully")
            
            elif student_found == True and field_found == False:
                print("Student Found But field Not exists")
            else:
                print("Student Not Exist")
                
        case 6: 
            break
        
        




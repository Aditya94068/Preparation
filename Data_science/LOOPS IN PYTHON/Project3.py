#Condition to create gmail
# adityavaishnav633@gmail.com
email = input("Enter a Email:")
k = 0
d = 0
z = 0
if len(email) >=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@") == 1):
            if(email[-4] == ".") ^(email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif  i.isalpha():
                        if i == i.upper():
                            d = 1
                    elif i.isdigit():
                        continue
                    elif i =="." or i =="_" or i == "@":
                        continue
                    else:
                        z = 1
                if k == 1 or d == 1 or z == 1:
                    print("Wrong Email 5")
                else:
                    print("Email is Correct : ",email)
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3 ")
    else:
        print("Wrong Email 2 ")
else:
    print("Wrong Email 1 ")
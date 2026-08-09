#Python main Har Chiz ek object hai 
# oop ka use kar ke program apne khud ke dataype create kar sakta hai
# Humne abhi tak jo bhi datatype pade python ke andar integer float list set dictionary tuple jo bhi humne pade ye sab classes hai python ke andar
# Create a ATM machine using oop
# ----------------------------------------------------------------------------------------------------------------------
# class ATM:
#     def __init__(self):
#         self.pin =''
#         self.balance = 0
#         self.menu()
#     def menu(self):
#         user_input = input("""
#         Hi how Can I Help You ?
#         1.Press 1 to Create pin
#         2.Press 2 to Change pin
#         3.Press 3 to Check balance
#         4.Press 4 to Withdraw
#         5.Anything else to exit
#         """)
#         if user_input =='1':
#             self.create_pin()
#         elif user_input =='2':
#             self.change_pin()
#         elif user_input == '3':
#             self.check_balance()
#         elif user_input == '4':
#             self.withdraw()
#         else:
#             exit()
#     def create_pin(self):
#         user_pin = input("Enter you pin :")
#         self.pin = user_pin

#         user_balance = int(input("Enter Balance :"))
#         self.balance = user_balance
        
#         print("Pin Created Successfully")
#         self.menu()
#     def change_pin(self):
#         old_pin = input("Enter your old pin :")
#         if self.pin == old_pin:
#             new_pin = input("Enter your new Pin :")
#             self.pin = new_pin
#             print("Pin Change Successfully")
#         else:
#             print("Please we can't allow you to change pin ")
#         self.menu()
#     def check_balance(self):
#         user_pin = input("Enter you pin :")
#         if user_pin == self.pin:
#             print("Your Balance :",self.balance)
#         else:
#             print("Wrong Pin , Please Enter the Correct Pin")
#         self.menu()
#     def withdraw(self):
#         user_pin = input("Enter you pin :")
#         if user_pin == self.pin:
#             amount = int(input("Enter you amount :"))
#             if amount <= self.balance:
#                 self.balance = self.balance - amount
#                 print("Withdraw amount :",amount)
#                 print("Amount In your Account :", self.balance)
#             else:
#                 print("You have not that much money in you account")
#         else:
#             print("Your Password is in Correct , Please Enter a Correct Password")
#         self. menu()
# obj = ATM()


# ----------------------------------------------------------------------------------------------------------------------
# Create aur own Fraction Data type using oop concept (like megic method or dunder method)

class Fraction:
    #parameterized Constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
       
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return '{}/{}'.format(new_num,new_den)
    
    def convert_to_decimal(self):
        return self.num/self.den
    
fr1 = Fraction(3,4)
fr2 = Fraction(1,2)

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)

ans = fr1.convert_to_decimal()
print(ans)












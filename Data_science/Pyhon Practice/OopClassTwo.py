# class Point:
#     def __init__(self,x,y):
#         self.x_cod = x
#         self.y_cod = y
#     def __str__(self):
#         return '<{},{}>'.format(self.x_cod,self.y_cod)
#     def euclidean_distance(self,other):
#         return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
#     def distance_from_orgin(self):
#         return (self.x_cod**2 + self.y_cod**2)**0.5
        # return self.euclidean_distance(Point(3,4))
# class Line:
#     def __init__(self,A,B,C):
#         self.A = A
#         self.B = B
#         self.C = C
#     def __str__(self):
#         return '{}X + {}Y + {} = 0'.format(self.A,self.B,self.C)
#     def point_on_line(line,point):
#         if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
#             return "Lies on the line"
#         else:
#             return "does not lie on the line"
#     def shortes_distance(line,point):
#        return abs(line.A * point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5
# # p1 = Point(3,4)
# # p2 = Point(10,10)
# # print(p1.euclidean_distance(p2))
# # print(p1.distance_from_orgin())
# L1 = Line(1,1,-2)
# p1 = Point(1,1)
# print(L1.point_on_line(p1)) # toh yha pe jo L1 object automatically hamara first input ban jata hai aur wo jake first wale ko milta hai
# print(L1.shortes_distance(p1)) 
# print(p1)


class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.__balance = 0
    #self.menu()

  def get_balance(self):
    return self.__balance

  def set_balance(self,new_value):
    if type(new_value) == int:
      self.__balance = new_value
    else:
      print('beta bahot maarenge')

  def __menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.__balance = user_balance

    print('pin created successfully')

  def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
    else:
      print('nai karne de sakta re baba')

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.__balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.__balance:
        self.__balance = self.__balance - amount
        print('withdrawl successful.balance is',self.__balance)
      else:
        print('abe garib')
    else:
      print('sale chor')
obj = Atm()
obj.get_balance()
obj.set_balance(1000)
obj.withdraw()



























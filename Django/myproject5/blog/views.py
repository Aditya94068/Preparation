from django.shortcuts import render
from datetime import datetime 
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
def home(request):
    context = {
        "name" : "Aditya Vaishnav",
        "age" : 21,
        "skill" : ['django', 'python', 'react'],
        "user" : User("vaishnav",30),
        "blog" :{
            "title" : "Django Template Into",
            "author" :{
                "name" : "Aditya",
            },
            "content" : "<b>This is Blog<\b>",
            "created_at" : datetime(2025,8,18,10,30),
        },
        "empty_value" : None,
    }
    return render(request,"blog/home.html",context)
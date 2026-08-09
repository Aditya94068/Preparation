from django.shortcuts import render
from datetime import datetime
def blog_list(request):
    blogs = [
        {"title":"Django Basics", "is_featured" :True,"author":"Aditya Vaishnav"},
        {"title":"Django Advance", "is_featured" :False,"author":""},
        {"title":"Django Rest Framework Basics", "is_featured" :False,"author":"Sumit Vaishnav"},
    ]
    context ={
        "blogs" : blogs,
        "today" : datetime.now(),
        "html_code" :"<b>Welcome to My Blogs</b>"
    }
    return render(request,'blog/blog_list.html',context)
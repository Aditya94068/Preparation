from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post={
        "title":"My Second Templates Post",
        "descriptions":"Django is a high-level Python Web framework that encourages rapid development and clean,pragmatic design.",
        "author":None,
        "created_at":datetime(2025,8,19,10,30),
        "comments_count":1,
        "tags":["Django","Python","Web Development"],
        "price":100,
        "number":7,
    }
    # jo bhi render karna hai wo iske andar mention karna important hai
    return render(request,"blog/blog_details.html",{"post" : post}) 
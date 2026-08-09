from django.shortcuts import render

def product_list(request):
    return render(request,'shop/product.html')
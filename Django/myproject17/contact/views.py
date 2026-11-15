from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact

def contact_form(request):
    return render(request,'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        created_at = request.POST.get('created')
        if name and message:
            Contact.objects.create(name=name,message=message)
            return HttpResponse(f"Thank you,{name},for your message at {created_at}!")
        else:
            return HttpResponse("Please provide both name and messages.")

    return redirect('contact_form')
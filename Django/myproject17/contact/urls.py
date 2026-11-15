from django.urls import path
from . import views
urlpatterns = [
    path('',views.contact_form,name='contact_from'),
    path('submit/',views.submit_contact,name='submit_contact'),
]
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def doctors(request):
    obj= Doctors.objects.all()
    return render(request,'doctors.html',{'obj':obj})

def specialities(request):
    obj= Departments.objects.all()
    return render(request,'specialities.html',{'obj':obj})



def booking(request):
     if request.method =="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')

     form = BookingForm()
     return render(request,'booking.html',{'form':form})



def callback_insert(request):
    if request.method =="POST":
        tc= Callback()
        tc.c_lname=request.POST.get("lname")
        tc.c_fname=request.POST.get("fname")
        tc.c_email=request.POST.get("email")
        tc.c_phone=request.POST.get("phone")
        tc.save()
        return redirect("/")


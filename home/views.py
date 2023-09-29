# from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .models import Product
from math import ceil
# Create your views here.
def index(request):
   products = Product.objects.all()
   print(products)
   n=len(products)
   nSlides = n//4 + ceil((n//4))-((n//4))
   params = {'no_of_slides':nSlides,'range':range(1,nSlides), 'product':products}
   return render(request,'index.html') 
def about(request):
   return render(request,'about.html') 
def services(request):
   return render(request,'service.html') 
def standard(request):
   return render(request,'standard.html')
def generic(request):
   return render(request,'generic.html')
def ayurvedic(request):
   return render(request,'ayurvedic.html')
def contact(request):
   if request.method=="POST":
      name=request.POST.get("name")
      email=request.POST.get("email")
      phone=request.POST.get("phone")
      desc=request.POST.get("desc")
      contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
      contact.save()
      messages.success(request, 'Your message has been sent !!!')
   return render(request,'contact.html') 
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib import messages

# Create your views here.
def index(request):
    item=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    return render(request,'gift/index.html',{'item':item,'categories':categories})
    
def contact(request):
    return render(request,'gift/contact.html')
    
def signupview(request):
       
       if request.method=="POST":
           form=SignupForm(request.POST)
           if form.is_valid():
               form.save()
               un=form.cleaned_data['username']
               messages.success(request,"You are successfully logged in as {}!!!!".format(un))
               return redirect('signin')
       elif request.method=="GET":
           form=SignupForm()
       return render(request,'gift/signup.html',{'form':form})
       
def aboutpage(request):
    return render(request,'gift/about.html')
def privacypage(request):
    return render(request,'gift/privacy.html')
def termpage(request):
    return render(request,'gift/term.html')
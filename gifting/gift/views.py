from django.shortcuts import render
from item.models import Category, Item

# Create your views here.
def index(request):
    item=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'gift/index.html',{'item':item,'categories':categories})
    
def contact(request):
    return render(request,'gift/contact.html')
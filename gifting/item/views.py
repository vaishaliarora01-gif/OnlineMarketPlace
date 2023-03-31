from django.shortcuts import render, get_object_or_404
from item.models import Item,Category

def details(request,pk):
      item=get_object_or_404(Item,pk=pk)
     # rel_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
      return render(request,'item/details.html',{'item':item})
    



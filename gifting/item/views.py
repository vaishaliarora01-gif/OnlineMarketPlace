from django.shortcuts import render, get_object_or_404,redirect
from item.models import Item,Category
from item.forms import NewItemForm


def details(request,pk):
      item=get_object_or_404(Item,pk=pk)
      rel_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
      return render(request,'item/details.html',{'item':item,'rel_items':rel_items})
    

def newItemview(request):
    
       if request.method=="POST":
           form=NewItemForm(request.POST, request.FILES)
           if form.is_valid():
               item=form.save(commit=False)
               item.created_by=request.user
               item.save()
               return redirect('item:details',pk=item.id)
       else :
            form=NewItemForm()
            return render(request,'item/form.html',{'form':form})


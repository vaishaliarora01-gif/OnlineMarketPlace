from django.shortcuts import render, get_object_or_404,redirect
from item.models import Item,Category
from item.forms import NewItemForm,EditItemForm
from django.http import HttpResponseBadRequest

def items(request):
    items=Item.objects.filter(is_sold=False)
    return render(request,'item/items.html',{'items':items})






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
            
            
            
def EditItemview(request,pk):
       item=get_object_or_404(Item,pk=pk)
       if request.method=="POST":
           form=EditItemForm(request.POST, request.FILES,instance=item)
           if form.is_valid():
               form.save()
               return redirect('item:details',pk=item.id)
           else:
               return HttpResponseBadRequest("Invalid form data")
       else :
            form=EditItemForm(instance=item)
            return render(request,'item/form.html',{'form':form})          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
   # return redirect('/myitems')
    return redirect('dashboard:myitems')
    


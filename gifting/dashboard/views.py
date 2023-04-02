from django.shortcuts import render,get_object_or_404
from item.models import Item

# Create your views here.
def dashboard_view(request):
    myitems=Item.objects.filter(created_by=request.user)
    return render(request,'dashboard/index.html',{'myitems':myitems})


from django.urls import path
from item import views
app_name='item'
urlpatterns=[
    path('<int:pk>/',views.details,name="details"),
    path('form/',views.newItemview,name="form"),
    path('<int:pk>/delete/',views.delete,name="delete"),
    path('<int:pk>/edit/',views.EditItemview,name="edit")
    ]
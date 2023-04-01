from django.urls import path
from item import views
app_name='item'
urlpatterns=[
    path('<int:pk>/',views.details,name="details"),
    path('form/',views.newItemview,name="form")
    ]
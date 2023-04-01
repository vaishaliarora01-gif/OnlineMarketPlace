from django.urls import path
from dashboard import views
app_name='dashboard'
urlpatterns=[
    path('myitems/',views.dashboard_view,name='myitems'),
    ]
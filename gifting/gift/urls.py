from django.urls import path
from . import views
app_name="gift"

urlpatterns=[
    path('',views.index, name='index'),
    path('/contact/',views.contact,name='contact'),
    path('signup/',views.signupview,name='signup'),
    path('about/',views.aboutpage,name='about'),
    path('privacy/',views.privacypage,name='privacy'),
    path('term/',views.termpage,name='term'),
    
    ]
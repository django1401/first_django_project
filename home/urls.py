from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('',home, name='home'),
    path('about',about, name='about'),
    path('contact',contact , name='contact'),
    path('blog',blog, name= 'blog'),
    path('blog-single',blog_single, name='blog-single'),

]
from django.urls import path
from .views import *



app_name='blog'

urlpatterns = [
    path('', blog_home , name='blog_home'),
    path('/tag/<str:tag>', blog_home , name='blog_home_with_tag'),
    path('/author/<str:username>', blog_home , name='blog_home_with_user'),
    path('/category/<str:cat>', blog_home , name='blog_home_with_cat'),
    path('/search/', blog_home , name='blog_home_with_search'),
]
from django.shortcuts import render
from django.views.generic import ListView

#python treats any imported py file as module where you can use classes of functions from
from .models import Post


class HomePageView(ListView):
    #we use a list view here because this is the data format returned from db

    model = Post  # this will create a list type object. 
                  #'post_list' name is automatically generated, using name of the model
    
    template_name = 'posts/home.html'
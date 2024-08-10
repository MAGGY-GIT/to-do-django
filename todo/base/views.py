from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#this will allow the views to show more information on the tasks in the models
from .models import Task
# Create your views here.


class TaskList(ListView):
     #I don't have to capitalize the class names always
     #we are inheriting from ListView as well as all ots functionalities
     model = Task
     context_object_name = "tasks"
     #this will create a context dictionary name rather than using the standard object_list


class TaskDetail(DetailView):
     model = Task
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task
# Create your views here.


class TaskList(ListView):
     #I don't have to capitalize the class names always
     #we are inheriting from ListView as well as all ots functionalities
     model = Task

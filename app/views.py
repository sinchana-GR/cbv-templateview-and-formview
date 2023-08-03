from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
# Create your views here.
from app.forms import *
from django.http import HttpResponse

# by using templateview class

class templatedatainsert(TemplateView):
    template_name='templatedatainsert.html' # html page

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ECO=super().get_context_data(**kwargs)  #empty dictionary context object
        SFO=Studentform() # collecting student form object
        ECO['SFO']=SFO # adding context to empty dictionary context object
        return ECO   # return that object with data 
    
    def post(self,request): # check for post method
        SFD=Studentform(request.POST) # collecting data from student form
        if SFD.is_valid(): # validating the data
            SFD.save() # save the data
            return HttpResponse('data is inserted by template form')
        

# by using formview class

class Studentformviewinsert(FormView): # by using formview class
    template_name='Studentformviewinsert.html'  # html page
    form_class=Studentform   # it will perform get context,called by super method,create form object,context will be added and it will return

    def form_valid(self, form):  # it will check for post method and collect the data and it will validate
        form.save() # in form the data will be stored then save it
        return HttpResponse('data is sent by view form')























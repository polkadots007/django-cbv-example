from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models
# Create your views here.

# def index(request):
#     return render(request, template_name='app/index.html')

class CBView(View):
    def get(self, request):
        return HttpResponse('Class based Views are here!')
    
class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context['myContent'] = 'Basic Injection'
        return context

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'app/school_detail.html'
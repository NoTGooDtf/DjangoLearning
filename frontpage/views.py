from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def landing_page_view(request):
  template = loader.get_template('frontpage.html')
  return HttpResponse(template.render())
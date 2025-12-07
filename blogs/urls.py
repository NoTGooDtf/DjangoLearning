from django.urls import path
from . import views

urlpatterns = [
    #in this things, blogs/ is implied at beginning.
    path('', views.blogs_page_view, name='landing_page'),
]
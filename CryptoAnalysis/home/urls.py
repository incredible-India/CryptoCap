from django.urls import path 
from . import views as ha
urlpatterns = [
  
  path('',ha.Index.as_view(),name="home")

]

from django.urls import path 
from . import views as ha
urlpatterns = [
  
  path('',ha.Index.as_view(),name="home"),
  path('/start/crypto/prediction',ha.prediction.as_view(),name="QORA-ANN")

]

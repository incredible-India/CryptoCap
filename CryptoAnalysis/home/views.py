from django.shortcuts import render

from django.db.models import Q

from django.views import View
# Create your views here.


#home page starting page

class Index(View):
    def get(self, request):
        return render(request, 'home/index.html');
from django.shortcuts import render
from django.views import generic

from .models import Blat

# Create your views here.
#def home(request):
#return render(request, 'balt/home.html', {'message':'Hello world'})

class IndexView(generic.ListView):
  template_name = 'balt/home.html'
  context_object_name = 'blat_list'

  def get_queryset(self):
    return Blat.objects.order_by('-create_on')[:20]

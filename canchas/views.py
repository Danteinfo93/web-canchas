from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Cancha
from .filters import CanchaFilter

# Create your views here.

class CanchaListView(ListView):

    model = Cancha
    #paginate_by = 100  

    def get_queryset(self):
        qs = self.model.objects.all()
        cancha_filtered_list = CanchaFilter(self.request.GET, queryset=qs)
        return cancha_filtered_list.qs

class CanchaDetailView(DetailView):

    model = Cancha
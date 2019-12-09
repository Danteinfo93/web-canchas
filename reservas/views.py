from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reserva
from .forms import ReservaModelForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator 
# Create your views here.

class ReservaListView(ListView):

    model = Reserva

class ReservaDetailView(DetailView):

    model = Reserva

@method_decorator(staff_member_required, name='dispatch')
class ReservaCreate(CreateView):
    model = Reserva
    form_class = ReservaModelForm
    success_url = reverse_lazy('reservas:list')

    def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.empleado = self.request.user
        reserva.save()
        return redirect(self.success_url)
    
    
@method_decorator(staff_member_required, name='dispatch')
class ReservaUpdate(UpdateView):
    model = Reserva
    form_class = ReservaModelForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('canchas:detail', args=[self.object.cancha.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ReservaDelete(DeleteView):
    model = Reserva

    def get_success_url(self):
        return reverse_lazy('canchas:detail', args=[self.object.cancha.id]) + '?ok_delete'
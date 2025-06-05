from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Mision, Astronauta, Experimento

# Misiones
class MisionList(ListView):
    model = Mision

class MisionCreate(CreateView):
    model = Mision
    fields = '__all__'
    success_url = reverse_lazy('mision_list')

class MisionUpdate(UpdateView):
    model = Mision
    fields = '__all__'
    success_url = reverse_lazy('mision_list')

class MisionDelete(DeleteView):
    model = Mision
    success_url = reverse_lazy('mision_list')

# Astronautas
class AstronautaList(ListView):
    model = Astronauta

class AstronautaCreate(CreateView):
    model = Astronauta
    fields = '__all__'
    success_url = reverse_lazy('astronauta_list')

class AstronautaUpdate(UpdateView):
    model = Astronauta
    fields = '__all__'
    success_url = reverse_lazy('astronauta_list')

class AstronautaDelete(DeleteView):
    model = Astronauta
    success_url = reverse_lazy('astronauta_list')

# Experimentos
class ExperimentoList(ListView):
    model = Experimento

class ExperimentoCreate(CreateView):
    model = Experimento
    fields = '__all__'
    success_url = reverse_lazy('experimento_list')

class ExperimentoUpdate(UpdateView):
    model = Experimento
    fields = '__all__'
    success_url = reverse_lazy('experimento_list')

class ExperimentoDelete(DeleteView):
    model = Experimento
    success_url = reverse_lazy('experimento_list')

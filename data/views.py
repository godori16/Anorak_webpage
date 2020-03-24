from django.views.generic import ListView, DetailView
from .models import Data

class DataListView(ListView):
    model = Data
    template_name = 'data.html'

class DataDetailView(DetailView):
    model = Data
    template_name = 'data_detail.html'

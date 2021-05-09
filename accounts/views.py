from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RegistrationForm

class RegistrationView(CreateView):
    model = RegistrationForm
    fields = '__all__'
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register_done')

class HomeView(ListView):
    model = RegistrationForm
    template_name = 'home.html'
    context_object_name = 'datas'

class RegisterDoneView(TemplateView):
    model = RegistrationForm
    template_name = 'registration/register_done.html'
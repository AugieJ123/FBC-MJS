from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import RegistrationView, HomeView, RegisterDoneView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('register/', RegistrationView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_dones.html'), name='password_done'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_forms.html', success_url = reverse_lazy('password_done')), name='change_password'),

]
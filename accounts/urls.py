from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import RegistrationView, HomeView, RegisterDoneView, DataUpdateView, DataDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html", redirect_authenticated_user=True), name='login'),

    path('register/', RegistrationView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_dones.html'), name='password_done'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_forms.html', success_url = reverse_lazy('password_done')), name='change_password'),

    path('data/<int:pk>/edit/', DataUpdateView.as_view(), name='data_edit'),
    path('data/<int:pk>/delete/', DataDeleteView.as_view(), name='data_delete'),

]

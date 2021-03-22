from django.urls import path
from django.conf.urls import url
from Users import views
from .views import signup, login, logout, edit_profile, profile_view, UsernameValidationView, EmailValidationView,VerificationView
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('profile/<username>', views.profile_view, name="profile"),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="registration/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="registration/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="registration/password_reset_done.html"),
         name="password_reset_complete"),

    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
    path('activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),

]
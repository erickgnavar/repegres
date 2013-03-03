from django.conf.urls import patterns, url

from accounts import views as a

urlpatterns = patterns('',

    url(r'login/$', a.LoginView.as_view(), name='login'),
    url(r'logout/$', a.LogoutView.as_view(), name='logout'),
    url(r'signup/$', a.RegisterView.as_view(), name='signup'),
    url(r'change_password/$', a.ChangePasswordView.as_view(), name='change_password'),
    url(r'reset_password/$', a.ResetPasswordView.as_view(), name='reset_password'),
)

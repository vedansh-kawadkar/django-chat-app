from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', view=views.frontpage, name='frontpage'),
    path('signup/', view=views.signup, name='signup'),
    path('logout/', view=auth_views.LogoutView.as_view(), name='logout'),
    path('login/', view=auth_views.LoginView.as_view(template_name='core/login.html'), name='login')
]

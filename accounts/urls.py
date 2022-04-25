from django.urls import path
from .views import CreateUserView, LoginView

urlpatterns = [
    ## Con el as_view() la clase funciona como una funcion en el archivo views.py
    path('registro/', CreateUserView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login')

]
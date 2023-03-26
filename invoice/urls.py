from django.urls import path
from . import views

app_name = 'invoice'
urlpatterns = [
    path('', views.index, name='index'),
    path('newinvoice/', views.saveInvoice, name='invoice')
]
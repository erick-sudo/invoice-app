from django.urls import path
from . import views

app_name = 'invoice'
urlpatterns = [
    path('all', views.index, name='index'),
    path('newinvoice/', views.saveInvoice, name='invoice'),
    path('pdf/', views.pdfInvoice, name='pdf') 
]
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Invoice, Business, Client
from django.core import serializers
import json

from django.http import HttpResponse

# Create your views here.
def index(request):
    #return render(request, 'link-invoice.html')
    invoices = serializers.serialize('json',Invoice.objects.all())
    return HttpResponse(invoices, content_type="text/json-comment-filtered")

class InvoiceView(generic.DetailView):
    model = Invoice
    template_name = 'invoice/invoice.html'

class Invoices(generic.ListView):
    template_name = 'invoice/invoice.html'
    context_object_name = 'invoice_list'

    def get_queryset(self):
        return Invoice.objects.all('-created_at')

def saveInvoice(request):
    business = Business.objects.create(business_name=request.POST['business_name'], email_address=request.POST['business_email'], address=request.POST['business_address'], website_link=request.POST['website'], business_no=request.POST['business_number'], business_phone=request.POST['business_phone'])

    client = Client.objects.create(full_name = request.POST['client_name'], email_address = request.POST['client_email'], address = request.POST['client_address'], phone = request.POST['client_phone'])

    invoice = Invoice.objects.create(business_id=business.pk, client_id=client.pk)

    return HttpResponse("Invoice Created")
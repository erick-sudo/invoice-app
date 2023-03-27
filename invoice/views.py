from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Invoice, Business, Client
from django.core import serializers
from reportlab.pdfgen    import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime

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
def pdfInvoice(request, invoice_id):
    print("PDF Invoice")

    invoice = get_object_or_404(Invoice, pk=invoice_id)
    business = get_object_or_404(Business, pk=invoice.business_id)
    client = get_object_or_404(Client, pk=invoice.client_id)


    print("Create the HttpResponse object")
    response = HttpResponse(content_type='application/pdf')

    print("Generate unique timestamp")
    timestamp = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')

    print("Force download")
    response['Content-Disposition'] = 'attachment; filename="INV_'+timestamp+'.pdf"'

    p = canvas.Canvas(response)

    print("Write content to PDF")

    logo = ImageReader('./leaf.png')
    img_width, img_height = logo.getSize()
    aspect = img_height / float(img_width)
    display_width = 100
    display_height = display_width * aspect

    print("Read Image")

    # A4 612/792
    p.drawImage(logo, 0, 792, width=display_width, height=display_height, mask='auto')

    print("Close the PDF object")
    p.showPage()
    p.save()

    print("Send back the PDF to the user")
    return response

def saveInvoice(request):
    print(request.POST)
    print("Saving Business")
    business = Business.objects.create(business_name=request.POST['business_name'], email_address=request.POST['business_email'], address=request.POST['business_address'], website_link=request.POST['website'], business_no=request.POST['business_number'], business_phone=request.POST['business_phone'])

    client = Client.objects.create(full_name = request.POST['client_name'], email_address = request.POST['client_email'], address = request.POST['client_address'], phone = request.POST['client_phone'])

    invoice = Invoice.objects.create(business_id=business.pk, client_id=client.pk)

    return HttpResponse("Invoice Created")
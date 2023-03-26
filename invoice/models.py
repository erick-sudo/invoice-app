from json import JSONEncoder
from django.db import models
import json

# Create your models here.

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    address = models.CharField(max_length=200)
    website_link = models.CharField(max_length=200)
    business_no = models.CharField(max_length=50)
    business_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.business_name
    
class Client(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

class Invoice(models.Model):
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)

    def inv_json(self):
        json.dumps(self, cls=InvoiceEncoder)

class InvoiceEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

class Item(models.Model):
    description = models.CharField(max_length=200)
    additional_description = models.CharField(max_length=200)
    rate = models.FloatField(default=0)
    taxable = models.BooleanField(default=False)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)

    def __str__(self):
        return self.description[:15]+"..."
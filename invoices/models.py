from customers.models import Customer

from django.db import models

from products.models import Product

class Invoice(models.Model):
    customer = models.ForeignKey(Customer)
    date_created = models.DateTimeField(auto_now_add = True)
    date_paid = models.DateField(blank = True, null = True)
    date_shipped = models.DateField(blank = True, null = True)
    tracking_number = models.CharField(max_length = 128, blank = True)
    notes = models.TextField(blank = True)

    def __unicode__(self):
        return "%d - %s %s" % (self.pk, self.customer, self.date_created)

class Item(models.Model):
    invoice = models.ForeignKey('invoices.Invoice')
    product = models.ForeignKey('products.Product')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits = 32, decimal_places = 2, blank = True, null = True)

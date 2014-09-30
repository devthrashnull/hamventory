from django.db import models

class Cost(models.Model):
    product = models.ForeignKey('products.Product')
    date = models.DateField()
    price = models.DecimalField(max_digits = 32, decimal_places = 2)

class Product(models.Model):
    name = models.CharField(max_length = 64, blank = True)
    price = models.DecimalField(max_digits = 32, decimal_places = 2)

    def __unicode__(self):
        return "%s" % (self.name)


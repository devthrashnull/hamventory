from django.db import models

from localflavor.us.models import USStateField, PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length = 32, blank = True)
    last_name = models.CharField(max_length = 32, blank = True)
    company_name = models.CharField(max_length = 32, blank = True)
    contact_name = models.CharField(max_length = 64, blank = True)
    group_id = models.CharField(max_length = 32, blank = True)
    
    address = models.CharField(max_length = 32)
    address2 = models.CharField(max_length = 32, blank = True)
    city = models.CharField(max_length = 32)
    state = USStateField()
    zip = models.CharField(max_length = 10)
    
    phone = PhoneNumberField()
    
    notes = models.TextField(blank = True)

    def __unicode__(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return "%s" % (self.company_name)

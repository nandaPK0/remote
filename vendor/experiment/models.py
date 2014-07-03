from django.db import models
from django.db.models.signals import m2m_changed 


class ProjectReport(models.Model):
    name = models.CharField(max_length=10, default='')

    def __unicode__(self):
        return self.name 


class TestFTP(models.Model):
    name = models.CharField(max_length=10, default='')
    file_address = models.FileField(upload_to='files/')
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.name 


class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)


def toppings_changed(sender, **kwargs):
    pass 

m2m_changed.connect(toppings_changed, sender=Pizza.toppings.through)






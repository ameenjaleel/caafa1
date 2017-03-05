from django.db import models

class Foodcort(models.Model):
    resto_name = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250)
    product_cuisines = models.CharField(max_length=250,blank=True)
    product_img = models.FileField(null=True, blank=True)
    product_about = models.TextField()
    product_price = models.IntegerField()

    def __unicode__(self):
        return self.resto_name

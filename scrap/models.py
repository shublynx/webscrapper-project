from django.db import models

# Create your models here.

class Linkmodel(models.Model):

    def __str__(self):
        return self.name

    address = models.CharField(max_length=500,blank=True,null=True)
    name = models.CharField(max_length=500,null=True)




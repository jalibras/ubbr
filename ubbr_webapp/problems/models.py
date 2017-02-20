from django.db import models
# Create your models here.

from django.urls import reverse

class ModelUbbr(models.Model):
    source = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('problem',args=[self.id])




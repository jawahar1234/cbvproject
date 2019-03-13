from django.db import models
from django.db import models
from django.urls import reverse


# Create your models here.
class book(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    pages = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})
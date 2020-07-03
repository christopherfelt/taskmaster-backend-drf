from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class List(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_lenth=50)
    color = models.CharField(max_length=10)
    
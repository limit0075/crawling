from django.db import models

# Create your models here.
class crawlingData(models.Model):
    commit_date = models.CharField(max_length= 100)
    commit_count = models.CharField(max_length= 100)
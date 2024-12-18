from django.db import models

# Create your models here.

class firstDB(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'mytool_firstdb'
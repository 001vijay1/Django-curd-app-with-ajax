from django.db import models
    
class Abc(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=20)
    score  = models.IntegerField()
    
    class Meta:
        managed =True
        db_table = 'abc'
        
from django.db import models

class studata1(models.Model):
    Name=models.CharField(max_length=25)
    Dept=models.CharField(max_length=20)
    Age=models.IntegerField()
    Mobile=models.BigIntegerField()
    Email=models.EmailField(max_length=15)
class subjects(models.Model):
    Student=models.CharField(max_length=20)
    Mark1=models.IntegerField()
    Mark2=models.IntegerField()
    Mark3=models.IntegerField()
    Mark4=models.IntegerField()

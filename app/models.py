from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.ename
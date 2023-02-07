from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=50)
    address = models.TextField( )
    year = models.IntegerField()

    def __str__(self) -> str:
        return self.sname
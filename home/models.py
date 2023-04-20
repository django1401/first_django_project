from django.db import models



#django-data-type
#geeksforgeeks

class student(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    avarage = models.DecimalField(max_digits=4,decimal_places=2)







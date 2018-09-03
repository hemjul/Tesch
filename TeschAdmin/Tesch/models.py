from django.db import models

# Create your models here.


class List_Of_Tesch_Users(models.Model):
    school_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    password = models.CharField(max_length=500)
    affliation = models.CharField(max_length=200)
    year_of_establishment = models.IntegerField()
    postal_code = models.CharField(max_length=6)
    school_landline=models.CharField(max_length=15)
    school_mobile = models.CharField(max_length=15)
    school_type= models.CharField(max_length=50)
    school_email= models.EmailField()
    account_creation_date = models.DateTimeField()
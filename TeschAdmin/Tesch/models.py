from django.contrib.auth.models import *
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class list_of_tesch_users():
    school_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,unique=True)
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
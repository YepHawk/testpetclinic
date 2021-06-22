from django.db import models

# Create your models here.
class Owners(models.Model):
    owner_id = models.CharField(max_length=4,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=80)
    telephone = models.CharField(max_length=20)

class Pets(models.Model):
    pet_id = models.CharField(max_length=4,unique=True)
    name = models.CharField(max_length=30)
    #bday =
    #type_id =
    owner_id = models.ForeignKey('Owners', on_delete=models.CASCADE)

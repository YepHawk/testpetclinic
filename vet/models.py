from django.db import models

# Create your models here.
class Owners(models.Model):
    owner_id = models.CharField(max_length=4,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=80)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        # managed = False
        db_table = 'Owners'

class Types(models.Model):
    type_id = models.CharField(max_length=4,primary_key=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        db_table = 'Types'


class Pets(models.Model):
    pet_id = models.CharField(max_length=4,primary_key=True)
    name = models.CharField(max_length=30)
    bday = models.DateField(null=True)
    owner = models.ForeignKey('Owners', on_delete=models.CASCADE)
    type = models.ForeignKey('Types', on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'Pets'

class Visits(models.Model):
    visit_id = models.CharField(max_length=4,primary_key=True)
    pet = models.ForeignKey('Pets', on_delete=models.CASCADE)
    visit_date = models.DateField(null=True)
    description = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'Visits'

class Vets(models.Model):
    vet_id = models.CharField(max_length=4,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        # managed = False
        db_table = 'Vets'

class VetSpec(models.Model):
    vet = models.ForeignKey('Vets', on_delete=models.CASCADE)
    spec = models.ForeignKey('Specialties', on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'VetSpec'

class Specialties(models.Model):
    spec_id = models.CharField(max_length=4,primary_key=True)
    name = models.CharField(max_length=80)

    class Meta:
        # managed = False
        db_table = 'Specialties'

from django.contrib import admin
from vet.models import Owners, Pets, Types, Visits, Vets, VetSpec, Specialties

# Register your models here.
admin.site.register(Owners)
admin.site.register(Pets)
admin.site.register(Types)
admin.site.register(Visits)
admin.site.register(Vets)
admin.site.register(VetSpec)
admin.site.register(Specialties)

from django import forms
from vet.models import Owners, Pets, Visits
from django.contrib.auth.forms import UserChangeForm

#currently unused...
class SearchOwner(forms.Form):
    lastname = forms.CharField(max_length=30)

class AddOwner(forms.ModelForm):
    class Meta:
        model = Owners
        fields = '__all__'

class AddPets(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ('pet_id','name','bday','type')

class EditOwner(UserChangeForm):
    class Meta:
        model = Owners
        fields = ('first_name','last_name','address','city','telephone')

class EditPet(UserChangeForm):
    class Meta:
        model = Pets
        fields = ('name','bday')

class AddVisit(forms.ModelForm):
    class Meta:
        model = Visits
        fields = ('visit_date','description')

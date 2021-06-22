from django import forms
from vet.models import Owners, Pets
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
        fields = '__all__'

class EditOwner(UserChangeForm):
    class Meta:
        model = Owners
        fields = '__all__'

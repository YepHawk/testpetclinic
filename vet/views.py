from django.shortcuts import render
from vet.forms import SearchOwner, AddOwner, AddPets, EditOwner, EditPet, AddVisit
from vet.models import Owners, Pets
#from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def findowners(request):
    if request.method == 'POST':
        searched = request.POST['searched'] #can be recoded with if statement so that if search is empty string, then show all owners, else, show what the string matches
        if len(searched) == 0:
            listofowners = Owners.objects.all()
        else:
            listofowners = Owners.objects.filter(last_name__contains=searched)
        return render(request,'findowners.html',{'listofowners':listofowners})
    else:
        return render(request,'findowners.html')

def ownerinfo(request, ownerid):
    owner = Owners.objects.get(owner_id=ownerid)
    return render(request,'ownerinfo.html',{'owner':owner})

def addowner(request):
    ownerForm = AddOwner()
    if request.method == "POST":
        ownerForm = AddOwner(request.POST)
        if ownerForm.is_valid():
            owner = ownerForm.save(commit=True)
            return render(request,'ownerinfo.html', {'owner':owner})
        else:
            print('Error: Invalid')
    return render(request,'addowner.html',{'owner':ownerForm})

def addpets(request, ownerid):
    owner = Owners.objects.get(owner_id=ownerid)
    pets = AddPets()
    if request.method == "POST":
        pets = AddPets(request.POST)
        if pets.is_valid():
            ownedpet = pets.save(commit=False)
            ownedpet.owner_id = ownerid
            ownedpet.save()
            return render(request,'ownerinfo.html',{'owner':owner})
        else:
            print('Error: Invalid')
    return render(request,'addpets.html',{'owner':owner,'pets':pets})

def ownereditor(request, ownerid):
    owner = Owners.objects.get(owner_id=ownerid)
    ownerform = EditOwner(request.POST or None, instance=owner)
    if ownerform.is_valid():
        ownerform.save()
        return render(request,'ownerinfo.html',{'owner':owner})
    else:
        print('Oh no...')
    return render(request,'ownereditor.html',{'owner':owner,'ownerform':ownerform})

def editpet(request, petid):
    pet = Pets.objects.get(pet_id=petid)
    petform = EditPet(request.POST or None, instance=pet)
    owner = Owners.objects.get(owner_id=pet.owner_id)
    if petform.is_valid():
        petform.save()
        return render(request,'ownerinfo.html',{'owner':owner})
    else:
        print('Oh no...')
    return render(request,'editpet.html',{'owner':owner,'petform':petform})

def addvisit(request, petid):
    pet = Pets.objects.get(pet_id=petid)
    owner = Owners.objects.get(owner_id=pet.owner_id)
    visitform = AddVisit(request.POST)
    if visitform.is_valid():
        vis = visitform.save(commit=False)
        vis.pet_id = petid
        vis.save()
        return render(request,'ownerinfo.html',{'owner':owner})
    return render(request,'addvisit.html',{'pet':pet,'visitform':visitform})

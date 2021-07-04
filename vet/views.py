from django.shortcuts import render
from vet.forms import SearchOwner, AddOwner, AddPets, EditOwner
from vet.models import Owners, Pets
#from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

# def findowners(request):
#     form = SearchOwner()
#     listofowners = []
#     if request.method == "POST":
#         form = SearchOwner(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['last_name'])
#             for person in Owners:
#                 if person.objects.(last_name) == form:
#                     print("working as intended")
#                     listofowners.append(person)
#     return render(request,'findowners.html', {'form':form})

# def findowners(request):
#
#     if request.method == "POST":
#         lnsearched = SearchOwner(request.POST)
#         print(lnsearched)
#         listofowners = Owners.objects.filter(last_name__contains=lnsearched)
#         return render(request,'findowners.html', {'lnsearched':lnsearched, 'listofowners':listofowners})
#
#     else:
#         form = SearchOwner()
#         return render(request,'findowners.html', {'form':form})

#def searchforowners(request):

def findowners(request):
    if request.method == 'POST':
        searched = request.POST['searched'] #can be recoded with if statement so that if search is empty string, then show all owners, else, show what the string matches
        listofowners = Owners.objects.filter(last_name__contains=searched)
        return render(request,'findowners.html',{'searched':searched,'listofowners':listofowners})
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
    print (owner)
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

    # def ownereditor(request, ownerid="Default"):
    #     if request.method =="POST":
    #         owner = EditOwner(request.POST, instance=request.Owner)
    #         if owner.is_valid():
    #             owner.save()
    #             return redirect('home.html')
    #     else:
    #         owner = EditOwner(instance=request.Owner)
    #         return render(request,'ownereditor.html',{'owner':owner})

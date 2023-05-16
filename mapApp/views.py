from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import coralReef


def map(request):
    coralReefPin = coralReef.objects.all()
    #print(coralReefPin.values_list('description', flat=True))
    context = {
        'coralReefPin': coralReefPin
    }
    return render(request, "map.html", context)


def listOfCoralReef(request):
    reefs = coralReef.objects.all()
    return render(request, 'listOfCoralReef.html', {'coral_reefs': reefs})


def addCoral(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        description = request.POST.get('description')

        coral_reef = coralReef(name=name, latitudeC=latitude, longitudeC=longitude, description=description)
        coral_reef.save()

        return redirect('map')

    else:
        return render(request, "addCoral.html")


def delete_coral_reef(request, reef_id):
    reef = coralReef.objects.get(id=reef_id)
    reef.delete()
    return redirect('listOfCoralReef')

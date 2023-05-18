from django.shortcuts import render,redirect
from .models import coralReef
from django.contrib.auth.decorators import login_required


@login_required
def map(request):
    coralReefPin = coralReef.objects.all()
    context = {
        'coralReefPin': coralReefPin,
        'userId': request.user.id
    }
    return render(request, "map.html", context)

@login_required
def listOfCoralReef(request):
    reefs = coralReef.objects.all()
    context = {
        'coral_reefs': reefs,
        'userId': request.user.id
    }
    return render(request, 'listOfCoralReef.html', context)

@login_required
def addCoral(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        description = request.POST.get('description')

        coral_reef = coralReef(name=name, latitudeC=latitude, longitudeC=longitude, description=description, observer_id=request.user.id)
        coral_reef.save()

        return redirect('map')

    else:
        return render(request, "addCoral.html")

@login_required
def delete_coral_reef(request, reef_id):
    reef = coralReef.objects.get(id=reef_id)
    reef.delete()
    return redirect('listOfCoralReef')





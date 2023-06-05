from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm


# Create your views here.
def homeCars(request):
    carModel = Car.objects.all()
    under4000 = carModel.filter(price__lte=4000)
    over4000 = carModel.filter(price__gte=4000)
    return render(request, "show_delete_exos/cars/homeCars.html", { "carModel": carModel, "under4000": under4000, "over4000": over4000 })


def createCar(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homeCars")
    else:
        form = CarForm()
    return render(request, "show_delete_exos/cars/createCar.html", { "form": form })


def destroyCar(request, id):
    destroy = Car(id)
    destroy.delete()
    return redirect("homeCars")
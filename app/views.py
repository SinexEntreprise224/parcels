from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import Parcels


def home(request):
    nb_colis = len(Parcels.objects.all())
    return  render(request, 'index.html', context={'nb_colis': nb_colis})

def parcels_page(request):
    return render(request, "parcels.html", context={"parcels": Parcels.objects.all()})

def add_parcel(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponse("success")
        return None
    else:
        form = AddForm()
        return render(request, "add.html", context={"forms": form})

def tracking_page(request, id):
    tracked_parcels = None
    error = None
    try:
        tracked_parcels = Parcels.objects.get(id=id)
    except Parcels.DoesNotExist:
        error = "Aucun colis avec ce id"
    return render(request, "tracking.html", context={"tracked_parcels": tracked_parcels, "error": error})

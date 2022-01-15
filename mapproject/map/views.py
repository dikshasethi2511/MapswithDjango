from django.shortcuts import render


# Create your views here.

# Takes web request -> returns web response

from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm
from django.http import HttpResponse
import folium
import geocoder

def index(request):
    #Creating forms
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            #Return to index page
            return redirect('/')
    else:
        #Render empty form
        form = SearchForm()

    #Getting the location
    #Getting last object from the database
    address_location = Search.objects.all().last()
    location = geocoder.osm(address_location)
    longitude = location.lng
    latitude = location.lat
    countryName = location.country

    #Checking for gibberish entry
    if latitude == None or longitude == None:
        #Deleting last entry
        address_location.delete()
        return HttpResponse('You have entered an incorrect location!')

    #Creating a map object
    mapObject = folium.Map(location=[19,-12], zoom_start=2)

    folium.Marker([latitude, longitude], tooltip='Check out the country!', popup=countryName).add_to(mapObject)
    #Converting to HTML representation
    mapObject = mapObject._repr_html_()
    context = { 'mapObject' : mapObject, 'form' : form}
    return render(request, 'index.html', context)

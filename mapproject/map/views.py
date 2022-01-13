from django.shortcuts import render


# Create your views here.

# Takes web request -> returns web response

from django.shortcuts import render
import folium
import geocoder

def index(request):
    #Getting the location
    location = geocoder.osm('UK')
    longitude = location.lng
    latitude = location.lat
    countryName = location.country
    #Creating a map object
    mapObject = folium.Map(location=[19,-12], zoom_start=2)
    folium.Marker([5.594, -0.219], tooltip='More for information!', popup='Ghana').add_to(mapObject)
    folium.Marker([latitude, longitude], tooltip='More for information!', popup=countryName).add_to(mapObject)
    #Converting to HTML representation
    mapObject = mapObject._repr_html_()
    context = { 'mapObject' : mapObject}
    return render(request, 'index.html', context)

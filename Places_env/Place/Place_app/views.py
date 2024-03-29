from django.shortcuts import render, render_to_response
import django.shortcuts
import datetime
from models import Place

#- list/- list descending date
def list_date(request):
    list_posts = Place.objects.all().order_by('date')
    return render_to_response('place/show_places.html',{'list_posts': list_posts })

#- - list the places by number of views
def list_nr_views(request):
    list_places_views = Place.objects.all().order_by('nr_views')
    return render_to_response('place/show_places.html',{'list_places_views': list_places_views})

# Detail Window
def detail(request, place_id):
    date = datetime.datetime.now()
    detail_place = Place.objects.get(id=place_id) 
    detail_place.nr_views =  detail_place.nr_views + 1
    detail_place.save()
    return render_to_response('place/show_places.html', {'detail_place': detail_place } )

# Main Window
def index(request):
    return render_to_response('place/main.html' )

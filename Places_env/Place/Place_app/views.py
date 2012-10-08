from django.shortcuts import render, render_to_response

import django.shortcuts
import datetime
from models import Place

#- list/- list descending date
def list_date(request):
    date = datetime.datetime.now()
#    list_posts = Place.objects.filter(date__gte = date).order_by('-date')
#    list_posts = Place.objects.all()
    list_posts = Place.objects.all().order_by('date')
    return render_to_response('place/show_places.html',{'list_posts': list_posts })

#- - list the places by number of views
def list_nr_views(request):
    date = datetime.datetime.now() - datetime.timedelta(5)
#    list_places_views = Place.objects.filter(date__gte = date).order_by('-date')
    list_places_views = Place.objects.all().order_by('nr_views')
    return render_to_response('place/show_places.html',{'list_places_views': list_places_views})

# Main Window 
def view(request):
    date = datetime.datetime.now()
    place = Place.objects.all().order_by('-date')
    return render_to_response('place/show_places.html', {'list_places_views': list_places_views} )

# Detail Window
# It show receive Id 
def detail(request, place_id):
    date = datetime.datetime.now()
    detail_place = Place.objects.get(id=place_id) # TODO: howto filter by id
    return render_to_response('place/show_places.html', {'detail_place': detail_place } )


def create(request):
    date = datetime.datetime.now()
    place = Place.objects.filter(date__gte = date).order_by('-date')
    return render_to_response('place/show_places.html',{'place': place})


def index(request):
    return render_to_response('place/main.html' )

def view_latest_places(request):
# Last 5 days
    date = datetime.datetime.now() - datetime.timedelta(5)
    posts = Place.objects.filter(date__gte = date).order_by('-date')
    return render_to_response('place/show_places.html',{'place': place})
#    
#- - list the places by: 1) descending date; 2) number of views
#- - view a place (viewing a place increments its number of views)

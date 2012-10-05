from django.shortcuts import render, render_to_response

#import django.shortcuts
import datetime
from models import Place

def create(request):
    date = datetime.datetime.now()
    place = Place.objects.filter(date__gte = date).order_by('-date')

    return render_to_response('place/show_places.html',{'place': place})
        
def list_date(request):
    date = datetime.datetime.now()
    posts = Place.objects.filter(date__gte = date).order_by('-date')
    return render_to_response('place/show_places.html',{'place': place})

def list_nr_views(request):
    date = datetime.datetime.now() - datetime.timedelta(5)
    posts = Place.objects.filter(date__gte = date).order_by('-date')
    return render_to_response('place/show_places.html',{'place': place})

def view(request):
    date = datetime.datetime.now()
    place = Place.objects.filter(date__gte = date).order_by('-date')
    return render_to_response('place/show_places.html' )


def view_latest_posts(request):
# Last 5 days
    date = datetime.datetime.now() - datetime.timedelta(5)
    posts = Place.objects.filter(date__gte = date).order_by('-date')
    return render_to_response('place/show_places.html',{'place': place})
#    
#- - list the places by: 1) descending date; 2) number of views
#- - view a place (viewing a place increments its number of views)

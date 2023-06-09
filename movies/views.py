"""views module"""
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def index(request):
    """returns http response"""
    movies  = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})
 
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    meetups = [
        {
            'title':'First Meet Up',
            'location':'Ghana','slug':
            'first-meetup'
        }
        ,
        
        {
            'title':'second Meet Up',
            'location':'New York',
            'slug':'second-meetup'},
    ]
    return render(request, "meet/index.html",{
        'meetups':meetups
    })


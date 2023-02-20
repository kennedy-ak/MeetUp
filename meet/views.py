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


def meetup_details(request,meetup_slug):
    print(meetup_slug) 
    selected_meetup ={
        'title':'A First Meetup',
        'description':'This is the First Meetup'
    }
    return render(request,"meet/meetup-details.html",{
        'meetup_title': selected_meetup['title'],
        'meetup_description':selected_meetup['description']
    })

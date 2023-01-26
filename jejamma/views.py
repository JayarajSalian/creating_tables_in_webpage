from django.shortcuts import render

# Create your views here.
from jejamma.models import *

def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpage(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    QSA=AccessRecords.objects.all()
    d={'access':QSA}
    return render(request,'display_accessrecords.html',d)
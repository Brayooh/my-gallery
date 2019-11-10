from django.shortcuts import render
from django.http import HttpResponse
from .models import image


def posted_images(request):

    pic = image.object.all()

    return render(request, 'index.html', {"pic":pic})


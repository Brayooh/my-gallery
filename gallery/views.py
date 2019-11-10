from django.shortcuts import render
from django.http import HttpResponse
from .models import image


def posted_images(request):

    pics = image.objects.all()

    return render(request, 'index.html', {"pics":pics})


def search_results(request):
    if 'pictures' in request.GET and request.GET["pictures"]:
        searched_term = request.GET.get("pictures")
        searched_pictures = image.search_by_title(searched_term)
        message = f"{searched_term}"

        return render(request, 'pic/search.html', {"message": message, "pictures": searched_pictures})

    else:
        message = "You have not searched for any picture"
        return render(request, 'pic/search.html', {"message": message})


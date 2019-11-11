from django.shortcuts import render
from django.http import HttpResponse
from .models import image


def posted_images(request):

    pics = image.objects.all()

    return render(request, 'index.html', {"pics":pics})

# def add_image(request):


#     return render(request, 'add_image.html')


def search_results(request):
    if 'pictures' in request.GET and request.GET["pictures"]:
        searched_term = request.GET.get("pictures")
        searched_pictures = image.search_by_category(searched_term)
        message = f"{searched_term}"

        return render(request, 'search.html', {"message": message, "pictures": searched_pictures})

    else:
        message = "You have not searched for any picture"
        return render(request, 'search.html', {"message": message})


# def copy_to_clipboard(request):
    
#     pyperclip.copy('The text to be copied to the clipboard.')
#     spam = pyperclip.paste()

#     return copy
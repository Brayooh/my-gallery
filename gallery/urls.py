from django.conf import settings
from . import views
from django.conf.urls import url
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$', views.posted_images, name='home'),
    url(r'^search/', views.search_results,name='search_results'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
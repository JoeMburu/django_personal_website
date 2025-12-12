from django.shortcuts import render
from django.conf import settings
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404
from .models import TestModel

# Create your views here.
def home(request):
    print("Default storage backend:", settings.STORAGES['default']['BACKEND'])

    # Grab an image from cloudinary storage
    images = TestModel.objects.all()
    
    context = {
        'images': images,
    }
    return render(request, 'home/home.html', context )
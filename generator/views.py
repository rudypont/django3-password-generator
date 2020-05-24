from django.shortcuts import render
from django.http import HttpResponse
import random
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def selectfile(request):
    return render(request, 'generator/selectfile.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        if fs.exists(uploaded_file.name):
            print('File exists. Deleting...')
            fs.delete(uploaded_file.name)
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'generator/upload.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('special'):
        characters.extend(list('@&é"(§è!çà)-'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

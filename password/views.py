from django.shortcuts import render
import random

def home(request):
    return render(request,"index.html")


def password(request):
    characters = list(request.GET.get('characters'))
    length = int(request.GET.get('length'))
    if request.GET.get('upper'):
        characters.extend(list('ASDFREWQ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@$_'))
    random_password = ''

    for i in range(length):
        random_password += random.choice(characters)

    return render(request,"pass.html",{'password' : random_password })
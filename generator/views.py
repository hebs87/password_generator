from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')


def password(request):
    # Create a list of the letters - takes each
    # letter and puts them into individual strings
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # If the user wants uppercase, we will add the
    # uppercase alphabet to the characters list
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # If the user wants special, we will add the
    # special characters to the characters list
    if request.GET.get('special'):
        characters.extend(list('!£$%^&*()@'))

    # If the user wants numbers, we will add the
    # numbers to the characters list
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    # We set the length to the value selected by the user
    # We also convert the length to an int
    # The second parameter is a default value
    length = int(request.GET.get('length', 12))

    user_password = ''

    # Loops through - number of loops is equivalent
    # to the length of the length variable
    for x in range(length):
        # For each loop, we add a random letter from
        # the characters list to the password
        user_password += random.choice(characters)

    context = {
        "password": user_password
    }

    return render(request, 'password.html', context)

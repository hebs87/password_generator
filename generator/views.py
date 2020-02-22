from django.shortcuts import render


# Create your views here.
def home(request):

    context = {
        'message': 'I love Django!'
    }

    return render(request, 'home.html', context)

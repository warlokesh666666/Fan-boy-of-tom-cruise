from django.shortcuts import render

# Create your views here.

def cruise(request):
    return render(request, 'wiki.html')
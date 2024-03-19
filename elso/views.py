from django.shortcuts import render

# Create your views here.

def elso_view(request):
    return render(request, 'index.html', {})


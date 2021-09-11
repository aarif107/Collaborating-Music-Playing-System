from django.shortcuts import render

# Frontend
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

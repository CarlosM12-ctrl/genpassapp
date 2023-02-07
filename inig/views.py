from django.shortcuts import render

# Create your views here.
def pagini(request):
    return render(request, "home.html")

def pagabo(request):
    return render(request, "about.html")
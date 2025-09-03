from django.shortcuts import render
from django.http import HttpResponse

def individual(request):
    context = {"title": "Individual", "user": "Nikita"}
    return render(request, "gui/individual.html", context)


# Create your views here.

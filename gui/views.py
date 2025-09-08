from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

# Erlaube nur bekannte Vorlagen (Schutz vor Pfad-Traversal)
ALLOWED_TEMPLATES = {
    "start": "start/index.html",
    "individual": "individual/index.html",
    "character": "character/index.html",
    "charity": "charity/index.html",
    "loop": "loop/index.html",
}

def start(request):
    return render(request, "start/index.html")

def site_view(request, slug: str):
    tpl = ALLOWED_TEMPLATES.get(slug)
    if not tpl:
        raise Http404("Unbekannte Vorlage")
    return render(request, tpl, {"slug": slug})


### Standard
# def start(request):
#     return render(request, "gui/start.html")

# def individual(request):
#     return render(request, "gui/individual.html")
###


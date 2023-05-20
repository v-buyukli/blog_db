from django.shortcuts import render


def index(request):
    context = "Blog page"
    return render(request, "index.html", {"context": context})

from django.shortcuts import render

# Create your views here.
def index(request):
    context = "Blog page"
    return render(request, "index.html", {"context": context})
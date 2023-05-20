from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from publications.models import Publication
from publications.forms import PublicationForm


def index(request):
    context = "Blog page"
    return render(request, "index.html", {"context": context})


def get_publication(request):
    publications_list = list(Publication.objects.all().values())
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            p_id = int(form.cleaned_data["publication_id"])
            return HttpResponseRedirect(reverse("publication_view", args=[p_id]))
    else:
        form = PublicationForm()

    context = {
        "form": form,
        "publications_list": publications_list,
    }
    return render(request, "publication.html", context)


def publication_view(request, p_id):
    try:
        p = Publication.objects.get(id=p_id)
    except Publication.DoesNotExist:
        return HttpResponseRedirect(reverse("publication"))
    return render(request, "publication_view.html", {"p": p})

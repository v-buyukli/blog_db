from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("publication/", views.get_publication, name="publication"),
    path("publication/<int:p_id>/", views.publication_view, name="publication_view"),
]

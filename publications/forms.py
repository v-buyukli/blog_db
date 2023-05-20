from django import forms
from django.core.exceptions import ValidationError

from publications.models import Publication


class PublicationForm(forms.Form):
    publication_id = forms.IntegerField(label="Publication number (id)", min_value=1)

    def clean_publication_id(self):
        publication_id = self.cleaned_data["publication_id"]
        if publication_id not in list(Publication.objects.all().values_list("id", flat=True)):
            raise ValidationError("This publication does not exist. Available numbers below")
        return publication_id

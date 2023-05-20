from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

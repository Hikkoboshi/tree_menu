from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Item(models.Model):
    menu = models.ForeignKey("Menu", related_name="items", on_delete=models.CASCADE)
    parent = models.ForeignKey("Item", related_name="items", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.menu} > {self.title}"

    def get_absolute_url(self):
        return reverse("main_slug", args=[self.slug])

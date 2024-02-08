from django.shortcuts import render

from menu.models import Item, Menu


def main(request, slug=None):
    return render(request, "main.html")

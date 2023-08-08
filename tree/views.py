from django.shortcuts import render
from django.views.generic import ListView
from .models import LinkInformation

class LinkList(ListView):
    model = LinkInformation
    ordering = '-pk'
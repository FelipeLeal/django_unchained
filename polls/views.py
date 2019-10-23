from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse


def index(request):
    date = datetime.datetime.today()
    return HttpResponse(f"Hello, world. You're at the polls index. {date}")

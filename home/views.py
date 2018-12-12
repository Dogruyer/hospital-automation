from django.shortcuts import render_to_response, render, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from authentico.models import User
import feedparser
# import xlrd, unicodedata'
import pandas as pd


def test(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "home/excel.html", c)
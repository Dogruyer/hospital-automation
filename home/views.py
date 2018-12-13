from django.shortcuts import render_to_response, render, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from authentico.models import User
import feedparser
# import xlrd, unicodedata'
import pandas as pd


def hasta_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/hasta_goruntule.html", c)


def hastane_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/hastane_goruntule.html", c)


def doktor_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/doktor_goruntule.html", c)


def idarikadro_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/idarikadro_goruntule.html", c)


def kullanici_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/kullanici_goruntule.html", c)


def hastalik_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/hastalik_goruntule.html", c)


def teshis_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/teshis_goruntule.html", c)


def ilac_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/ilac_goruntule.html", c)


def recete_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/recete_goruntule.html", c)


def randevu_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/randevu_goruntule.html", c)


def klinik_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/klinik_goruntule.html", c)


def yonetici_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/yonetici_goruntule.html", c)


def izinler_goruntule(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "goruntule/izinler_goruntule.html", c)


def yeni_hasta(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_hasta.html", c)


def yeni_hastane(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_hastane.html", c)


def yeni_doktor(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_doktor.html", c)


def yeni_idarikadro(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_idarikadro.html", c)


def yeni_kullanici(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_kullanici.html", c)


def yeni_hastalik(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_hastalik.html", c)


def yeni_teshis(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_teshis.html", c)


def yeni_ilac(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_ilac.html", c)


def yeni_recete(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_recete.html", c)


def yeni_randevu(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_randevu.html", c)


def yeni_klinik(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_klinik.html", c)


def yeni_yonetici(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_yonetici.html", c)


def yeni_izinler(request):
    c = {"request": request}
    c.update(csrf(request))

    return render(request, "yeni/yeni_izinler.html", c)
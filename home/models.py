from django.db import models


class Hasta(models.Model):
    adi = models.CharField(max_length=100)
    yas = models.IntegerField()
    cinsiyet = models.CharField(max_length=100)
    tc_kimlik_no = models.CharField(max_length=100)


class Hastane(models.Model):
    adi = models.CharField(max_length=100)
    lokasyon = models.CharField(max_length=100)
    sahibi = models.CharField(max_length=100)


class Doktor(models.Model):
    adi = models.CharField(max_length=100)
    yas = models.IntegerField()
    cinsiyet = models.CharField(max_length=100)
    tc_kimlik_no = models.CharField(max_length=100)
    brans = models.CharField(max_length=100)
    unvan = models.CharField(max_length=100)
    bolum = models.CharField(max_length=100)
    hastane = models.ForeignKey(Hastane)


class IdariKadro(models.Model):
    adi = models.CharField(max_length=100)
    yas = models.IntegerField()
    cinsiyet = models.CharField(max_length=100)
    unvan = models.CharField(max_length=100)
    bolum = models.CharField(max_length=100)
    hastane = models.ForeignKey(Hastane)


class Kullanici(models.Model):
    adi = models.CharField(max_length=100)
    yas = models.IntegerField()
    cinsiyet = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    tc_kimlik_no = models.CharField(max_length=100)
    aktif = models.BooleanField(default=True)
    yonetici = models.BooleanField(default=True)


class Hastalik(models.Model):
    adi = models.CharField(max_length=100)
    bolum = models.CharField(max_length=100)


class Teshis(models.Model):
    adi = models.CharField(max_length=100)
    hastalik = models.ForeignKey(Hastalik)


class Ilac(models.Model):
    adi = models.CharField(max_length=100)


class Recete(models.Model):
    numara = models.CharField(max_length=100)
    hasta = models.ForeignKey(Hasta)
    ilac = models.ForeignKey(Ilac)


class Randevu(models.Model):
    doktor = models.ForeignKey(Doktor)
    hasta = models.ForeignKey(Hasta)
    hastane = models.ForeignKey(Hastane)


class Klinik(models.Model):
    adi = models.CharField(max_length=100)
    lokasyon = models.CharField(max_length=100)


class Yonetici(models.Model):
    adi = models.CharField(max_length=100)
    yas = models.IntegerField()
    cinsiyet = models.CharField(max_length=100)


class Izinler(models.Model):
    adi = models.CharField(max_length=100)
    turu = models.CharField(max_length=100)
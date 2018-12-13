from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^hasta_goruntule$',
                           'home.views.hasta_goruntule',
                           name='hasta_goruntule'),

                       url(r'^hastane_goruntule$',
                           'home.views.hastane_goruntule',
                           name='hastane_goruntule'),

                       url(r'^doktor_goruntule$',
                           'home.views.doktor_goruntule',
                           name='doktor_goruntule'),

                       url(r'^idarikadro_goruntule$',
                           'home.views.idarikadro_goruntule',
                           name='idarikadro_goruntule'),

                       url(r'^kullanici_goruntule$',
                           'home.views.kullanici_goruntule',
                           name='kullanici_goruntule'),

                       url(r'^hastalik_goruntule$',
                           'home.views.hastalik_goruntule',
                           name='hastalik_goruntule'),

                       url(r'^teshis_goruntule$',
                           'home.views.teshis_goruntule',
                           name='teshis_goruntule'),

                       url(r'^ilac_goruntule$',
                           'home.views.ilac_goruntule',
                           name='ilac_goruntule'),

                       url(r'^recete_goruntule$',
                           'home.views.recete_goruntule',
                           name='recete_goruntule'),

                       url(r'^randevu_goruntule$',
                           'home.views.randevu_goruntule',
                           name='randevu_goruntule'),

                       url(r'^klinik_goruntule$',
                           'home.views.klinik_goruntule',
                           name='klinik_goruntule'),

                       url(r'^yonetici_goruntule$',
                           'home.views.yonetici_goruntule',
                           name='yonetici_goruntule'),

                       url(r'^izinler_goruntule$',
                           'home.views.izinler_goruntule',
                           name='izinler_goruntule'),

                       url(r'^yeni_hasta$',
                           'home.views.yeni_hasta',
                           name='yeni_hasta'),

                       url(r'^yeni_hastane$',
                           'home.views.yeni_hastane',
                           name='yeni_hastane'),

                       url(r'^yeni_doktor$',
                           'home.views.yeni_doktor',
                           name='yeni_doktor'),

                       url(r'^yeni_idarikadro$',
                           'home.views.yeni_idarikadro',
                           name='yeni_idarikadro'),

                       url(r'^yeni_kullanici$',
                           'home.views.yeni_kullanici',
                           name='yeni_kullanici'),

                       url(r'^yeni_hastalik$',
                           'home.views.yeni_hastalik',
                           name='yeni_hastalik'),

                       url(r'^yeni_teshis$',
                           'home.views.yeni_teshis',
                           name='yeni_teshis'),

                       url(r'^yeni_ilac$',
                           'home.views.yeni_ilac',
                           name='yeni_ilac'),

                       url(r'^yeni_recete$',
                           'home.views.yeni_recete',
                           name='yeni_recete'),

                       url(r'^yeni_randevu$',
                           'home.views.yeni_randevu',
                           name='yeni_randevu'),

                       url(r'^yeni_klinik$',
                           'home.views.yeni_klinik',
                           name='yeni_klinik'),

                       url(r'^yeni_yonetici$',
                           'home.views.yeni_yonetici',
                           name='yeni_yonetici'),

                       url(r'^yeni_izinler$',
                           'home.views.yeni_izinler',
                           name='yeni_izinler'),

                       # url(r'^hospitalautomation/',
                       #     include('hospitalautomation.foo.urls')),
)

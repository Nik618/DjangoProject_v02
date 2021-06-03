from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from .views import *

urlpatterns = [  # вложенный список маршрутов через include
    path('admin/', admin.site.urls),
    path('get/country/', GetCountry.as_view()),
    path('set/country/<str:pk>', SetCountry.as_view()),

    path('get/town/', GetTown.as_view()),
    path('set/town/<str:pk>', SetTown.as_view()),

    path('get/capital/', GetCapital.as_view()),
    path('set/capital/<str:pk>', SetCapital.as_view()),

    path('get/<tittle>/', getTowns.as_view()),
    # path('get__/<location>', getObject.as_view()),

    re_path('get/town/(?P<c1>-?\d*\,-?\d*)/(?P<c2>-?\d*\,-?\d*)/(?P<c3>-?\d*\,-?\d*)/(?P<c4>-?\d*\,-?\d*)/$',
            getTownInArea.as_view()),  # города внутри области get/town/-1000,-1000/100,100/1000,1000/10000,10000/
    re_path('get/country/(?P<c1>-?\d*\,-?\d*)/(?P<c2>-?\d*\,-?\d*)/(?P<c3>-?\d*\,-?\d*)/(?P<c4>-?\d*\,-?\d*)/$',
            getCountryInArea.as_view()),  # страны внутри области get/town/-1000,-1000/100,100/1000,1000/10000,10000/
    re_path('get/capital/(?P<c1>-?\d*\,-?\d*)/(?P<c2>-?\d*\,-?\d*)/(?P<c3>-?\d*\,-?\d*)/(?P<c4>-?\d*\,-?\d*)/$',
            getCapitalInArea.as_view()),  # столицы внутри области get/town/-1000,-1000/100,100/1000,1000/10000,10000/

    re_path('get/town/square/(?P<c1>-?\d*\,-?\d*)/(?P<c2>-?\d*\,-?\d*)/(?P<c3>-?\d*\,-?\d*)/(?P<c4>-?\d*\,-?\d*)/$', getSquare.as_view()),  # площадь
]

urlpatterns = format_suffix_patterns(urlpatterns)

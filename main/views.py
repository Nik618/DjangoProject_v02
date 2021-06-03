from django.contrib.gis.geos import MultiPolygon, Polygon
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework_gis.pagination import GeoJsonPagination

from .models import Country, Town, Capital

from django.views.generic.edit import CreateView
from django.core.serializers import serialize
from django.http import HttpResponse
from django.core.serializers import serialize
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *


# Create your views here.
# def countryDatasets(request):
#     red = serialize('geojson',
#                     Country.objects.all(),
#                     geometry_field='location')
#     return Response(red)


class GetCountry(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AddCountry(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SetCountry(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DelCountry(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class GetTown(generics.ListAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class AddTown(generics.CreateAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class SetTown(generics.RetrieveUpdateAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class DelTown(generics.RetrieveDestroyAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class GetCapital(generics.ListAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer


class AddCapital(generics.CreateAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer


class SetCapital(generics.RetrieveUpdateAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer


class DelCapital(generics.RetrieveDestroyAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer

    # def get_queryset(self):
    #    queryset = Town.objects.all()
    #    country = self.kwargs['Russia']
    #    if country is not None:
    #        queryset = Town.objects.filter(country=country)
    #    return queryset


class getTowns(generics.ListAPIView):
    serializer_class = TownSerializer

    def get_queryset(self):
        param = self.kwargs['tittle']
        return Town.objects.filter(country__tittle=param)


class getTownInArea(generics.ListAPIView):  # вывести объекты, находящиеся внутри области
    queryset = Town.objects.all()
    serializer_class = TownSerializer

    def getC(self, c: str) -> tuple:
        return tuple(float(i) for i in c.split(','))

    def get(self, request, c1, c2, c3, c4):
        c1 = self.getC(c1)
        c2 = self.getC(c2)
        c3 = self.getC(c3)
        c4 = self.getC(c4)
        search_area = MultiPolygon(Polygon((c1, c2, c3, c4, c1,)))
        paginator = GeoJsonPagination()
        paginator.page_size = 3
        red = Town.objects.filter(location__contained=search_area)  # ключевой момент
        result_page = paginator.paginate_queryset(red, request)
        serializer = TownSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class getCountryInArea(generics.ListAPIView):  # вывести объекты, находящиеся внутри области
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def getC(self, c: str) -> tuple:
        return tuple(float(i) for i in c.split(','))

    def get(self, request, c1, c2, c3, c4):
        c1 = self.getC(c1)
        c2 = self.getC(c2)
        c3 = self.getC(c3)
        c4 = self.getC(c4)
        search_area = MultiPolygon(Polygon((c1, c2, c3, c4, c1,)))
        paginator = GeoJsonPagination()
        paginator.page_size = 3
        red = Country.objects.filter(location__contained=search_area)  # ключевой момент
        result_page = paginator.paginate_queryset(red, request)
        serializer = CountrySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class getCapitalInArea(generics.ListAPIView):  # вывести объекты, находящиеся внутри области
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer

    def getC(self, c: str) -> tuple:
        return tuple(float(i) for i in c.split(','))

    def get(self, request, c1, c2, c3, c4):
        c1 = self.getC(c1)
        c2 = self.getC(c2)
        c3 = self.getC(c3)
        c4 = self.getC(c4)
        search_area = MultiPolygon(Polygon((c1, c2, c3, c4, c1,)))
        paginator = GeoJsonPagination()
        paginator.page_size = 3
        red = Capital.objects.filter(location__contained=search_area)  # ключевой момент
        result_page = paginator.paginate_queryset(red, request)
        serializer = CapitalSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class getS(generics.ListAPIView):  # вывести площадь
    queryset = Town.objects.all()
    serializer_class = TownSerializer

    def getC(self, c: str) -> tuple:
        return tuple(float(i) for i in c.split(','))

    def get(self, request, c1, c2, c3, c4):
        c1 = self.getC(c1)
        c2 = self.getC(c2)
        c3 = self.getC(c3)
        c4 = self.getC(c4)
        search_area = MultiPolygon(Polygon((c1, c2, c3, c4, c1,)))
        paginator = GeoJsonPagination()
        paginator.page_size = 3
        red = Town.objects.filter(location__contained=search_area)  # ключевой момент
        sumS = 0
        for town in red:
            sumS += town.location.area
        return HttpResponse(content=sumS)




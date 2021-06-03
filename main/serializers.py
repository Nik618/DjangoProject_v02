from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Country, Town, Capital


class CountrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Country
        fields = ['tittle', 'location']
        geo_field = 'location'


class TownSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Town
        fields = ['tittle', 'description', 'photos', 'location', 'country']
        geo_field = 'location'


class CapitalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Capital
        fields = ['tittle', 'location', 'country']
        geo_field = 'location'


class Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Capital
        fields = ['tittle', 'location', 'country']
        geo_field = 'location'

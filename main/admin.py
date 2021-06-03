from django.contrib import admin
from .models import Country, Town, Capital
from leaflet.admin import LeafletGeoAdmin


# Register your models here.
class CountryAdmin(LeafletGeoAdmin):
    list_display = ('tittle', 'location')
    list_display_links = ('tittle', 'location')
    search_fields = ('tittle', 'location')


class TownAdmin(LeafletGeoAdmin):
    list_display = ('tittle', 'description', 'photos', 'location', 'country')
    list_display_links = ('tittle', 'description', 'photos', 'location', 'country')
    search_fields = ('tittle', 'description', 'photos', 'location', 'country')


class CapitalAdmin(LeafletGeoAdmin):
    list_display = ('tittle', 'location', 'country')
    list_display_links = ('tittle', 'location', 'country')
    search_fields = ('tittle', 'location', 'country')


class ObjAdmin(LeafletGeoAdmin):
    list_display = ('tittle', 'location')


admin.site.register(Country, CountryAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(Capital, CapitalAdmin)

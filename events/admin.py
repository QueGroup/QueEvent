from django.contrib import admin
from django_admin_geomap import ModelAdmin

# Register your models here.

from .models import Event, EventType, EventLocation


class EventAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'content',
                    'published',
                    'event_type')
    list_display_links = ('title',
                          'content')
    search_fields = ('title', 'content',)


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(EventLocation, Admin)

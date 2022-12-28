from django.contrib import admin

# Register your models here.

from .models import Event, EventType


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


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)

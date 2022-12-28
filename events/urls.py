from django.urls import path

from events.views import index, by_event_type

urlpatterns = [
    path('<int:event_type_id>/', by_event_type, name='by_event_type'),
    path('', index, name='index')
]

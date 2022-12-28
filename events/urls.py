from django.urls import path

from events.views import index, by_event_type, EventCreateView

urlpatterns = [
    path('add/', EventCreateView.as_view(), name='add'),
    path('<int:event_type_id>/', by_event_type, name='by_event_type'),
    path('', index, name='index')
]

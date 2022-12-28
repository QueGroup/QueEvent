from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from events.models import Event, EventType


# Create your views here.
def index(request):
    events = Event.objects.order_by('-published')
    event_types = EventType.objects.all()
    context = {'events': events, 'event_types': event_types}
    return render(request, 'events/index.html', context)


def by_event_type(request, event_type_id):
    events = Event.objects.filter(event_type=event_type_id)
    event_types = EventType.objects.all()
    current_event_type = EventType.objects.get(pk=event_type_id)
    context = {'events': events, 'event_types': event_types,
               'current_event_type': current_event_type}
    return render(request, 'events/by_event_type.html', context)

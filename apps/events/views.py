from django.shortcuts import render, get_object_or_404

from .models import Event

def event_list(request):

 events = Event.objects.filter(
    status="published"
)

 return render(
    request,
    "events/event_list.html",
    {
        "events": events
    }
)

def event_detail(request, slug):

 event = get_object_or_404(
    Event,
    slug=slug,
    status="published"
)

 return render(
    request,
    "events/event_detail.html",
    {
        "event": event
    }
)
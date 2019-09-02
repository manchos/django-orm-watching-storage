from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def format_duration(duration_seconds):
    hours = round(duration_seconds // 3600)
    minutes = round((duration_seconds % 3600) // 60)
    return '{}ч {}мин'.format(hours, minutes)


def storage_information_view(request):
    all_active_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = [
        {
            "who_entered": visit.passcard.owner_name,
            "entered_at": '{:%d-%m-%Y %H:%M}'.format(visit.entered_at),
            "duration": format_duration(visit.get_duration()), #"25:03",
        } for visit in all_active_visits
    ]

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

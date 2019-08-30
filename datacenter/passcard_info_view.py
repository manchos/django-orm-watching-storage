from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def format_duration(duration_seconds):
    hours = round(duration_seconds // 3600)
    minutes = round((duration_seconds % 3600) // 60)
    return '{}ч {}мин'.format(hours, minutes)


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    # Программируем здесь
    passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = [
        {
            "entered_at": '{:%d-%m-%Y}'.format(
                timezone.localtime(visit.entered_at)),
            "duration": format_duration(visit.get_duration()),
            "is_strange": visit.is_long()
        } for visit in passcard_visits
    ]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


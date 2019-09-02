from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def active_passcards_view(request):
    all_passcards = Passcard.objects.order_by("-created_at").filter(
        is_active=True)
    all_entered_visits = Visit.objects.filter(leaved_at__isnull=True)
    context = {
        "active_passcards": all_passcards,
    }

    return render(request, 'active_passcards.html', context)

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def active_passcards_view(request):
    # Программируем здесь

    # all_passcards = Passcard.objects.all()
    all_passcards = Passcard.objects.filter(is_active=True)
    all_visits = Visit.objects.all()
    all_entered_visits = Visit.objects.filter(leaved_at__isnull=True)
    context = {
        "active_passcards": all_passcards,  # люди с активными пропусками
    }

    for visit in all_entered_visits:
      # visit.leaved_at - visit.entered_at if visit.leaved_at else
      # if not visit.leaved_at:
      delta_time = timezone.localtime(timezone.now()) - timezone.localtime(visit.entered_at)
      print(
        '{name} '
        'зашёл в хранилище, время по Москве: {enter_dtime} \n'
        'Находится в хранилище: {remain_time}'.format(
          name=visit.passcard.owner_name,
          enter_dtime=timezone.localtime(visit.entered_at),
          remain_time=delta_time)
      )



    return render(request, 'active_passcards.html', context)

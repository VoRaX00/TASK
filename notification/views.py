from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from .models import NotifyHomework


def get_context(notifications, request):
    paginator = Paginator(notifications, per_page=4)
    page_number = request.GET.get('page')
    objects = paginator.get_page(page_number)

    context = {
        'page_obj': objects
    }
    return context


def my_notification(request):
    if request.POST:
        if request.POST.get('accept_id'):
            homework_id = request.POST.get('accept_id')
            notify = NotifyHomework.objects.get(id=homework_id)
            notify.status_second_user = 'y'
            notify.save()
        else:
            homework_id = request.POST.get('reject_id')
            notify = NotifyHomework.objects.get(id=homework_id)
            notify.status_second_user = 'n'
            notify.save()

    notifications = NotifyHomework.objects.all().filter(second_user=request.user).filter(
        status_second_user='u').order_by("-id")

    context = get_context(notifications, request)
    return render(request, 'my_notification.html', context=context)


def my_response(request):
    if request.POST:
        if request.POST.get('homework_id'):
            homework_id = request.POST.get('homework_id')
            notify = NotifyHomework.objects.get(id=homework_id)
            notify.delete()

    notifications = NotifyHomework.objects.all().filter(first_user=request.user).order_by("-id")

    context = get_context(notifications, request)
    return render(request, 'my_responses.html', context=context)


def my_match(request):
    notifications = NotifyHomework.objects.all().filter(
        Q(first_user=request.user) | Q(second_user=request.user)).filter(status_first_user='y').filter(
        status_second_user='y')

    context = get_context(notifications, request)
    return render(request, 'my_match.html', context=context)

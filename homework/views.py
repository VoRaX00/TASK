from django.shortcuts import render
from django.utils import timezone
from .models import Homework
from django.core.paginator import Paginator


def view_homework(request):
    search_name = ''
    if request.POST:
        search_name = request.POST.get('search_input')

    user_id = request.user.id
    if search_name != '':
        today = timezone.now().date()
        cargs = Homework.objects.all().filter(name=search_name).filter(loading_data__gt=today).select_related(
            'user_id').exclude(user_id=user_id).order_by(
            '-id')
    else:
        today = timezone.now().date()
        cargs = Homework.objects.all().filter(loading_data__gt=today).select_related('user_id').exclude(
            user_id=user_id).order_by('-id')

    paginator = Paginator(cargs, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'viewHomework.html', context=context)

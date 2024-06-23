from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Homework
from django.core.paginator import Paginator
from notification.models import NotifyHomework


def view_homework(request):
    search_name = ''
    if request.POST:
        search_name = request.POST.get('search_input')

    if search_name != '':
        today = timezone.now().date()
        homeworks = Homework.objects.all().filter(name=search_name).filter(deadline__gte=today).select_related(
            'user').exclude(user=request.user).order_by(
            '-id')
    else:
        today = timezone.now().date()
        homeworks = Homework.objects.all().filter(deadline__gte=today).select_related('user').exclude(
            user=request.user).order_by('-id')

    paginator = Paginator(homeworks, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'view_homework.html', context=context)


def add_homework(request):
    if request.POST:
        subjects = request.POST.getlist('subject')
        print(subjects)
        homework = Homework(name=request.POST['homework'], description=request.POST['description'], subjects=subjects,
                            user=request.user, difficulty=request.POST['difficulty'], rating=request.POST['rating'],
                            deadline=request.POST['deadline'])
        homework.save()
        return redirect('homework:view_homework')
    return render(request, 'add_homework.html')


def add_response(request):
    id = request.POST.get('homework_id')
    hw = Homework.objects.get(id=id)
    if request.user == hw.user:
        return redirect('homework:view_homework')

    notify = NotifyHomework(homework=hw, first_user=request.user, second_user=hw.user)
    notify.save()
    return redirect('homework:view_homework')

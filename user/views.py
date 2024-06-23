from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
# from car_cargo.models import Cargo, Car
# from car_cargo.views import array_cars
from django.core.paginator import Paginator
# from notification.views import objects_notify
from django.utils import timezone


def checking_name_email(request, email, name):
    if User.objects.filter(email=email):
        messages.error(request, 'Аккаунт для указанной электронной почты уже существует')
        return False

    if len(name) > 255:
        messages.error(request, 'Имя слишком длинное')
        return False

    if not name.isalnum():
        messages.error(request, 'Имя может состоять только из цифр и букв')
        return False
    return True


User = get_user_model()


def login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            dj_login(request, user)
            return render(request, 'profile.html')
        else:
            messages.error(request, "Bad credentials")
            return render(request, 'index.html')

    return render(request, 'login.html')


def logout(request):
    dj_logout(request)
    messages.success(request, "Logged")
    return redirect('main:index')


def registration(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not checking_name_email(request, email, name):
            return redirect('user:registration')

        if password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('user:registration')

        user = User.objects.create_user(name=name, email=email, password=password1)
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        mail_subject = 'Ссылка на активацию была отправлена на вашу электронную почту'

        message = render_to_string('activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        email_msg = EmailMessage(mail_subject, message, to=[email])
        email_msg.send()
        return render(request,
                      'send_message_email.html')

    return render(request, 'registration.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Спасибо, что зарегистрировали свой аккаунт!')
    else:
        return HttpResponse('Activation link is invalid!')


def profile(request):
    if request.POST:
        return render(request, 'edit_profile.html')
    today = timezone.now().date()
    # my_cargs = Cargo.objects.all().filter(user_id=request.user).filter(loading_data__gt=today).order_by('-id')
    # my_cars = Car.objects.all().filter(user=request.user).filter(ready_from__gt=today).order_by('-id')
    # cars = array_cars(my_cars)
    # objects = objects_notify(my_cargs, cars)

    # paginator = Paginator(objects, per_page=5)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # context = {'page_obj': page_obj}

    return render(request, 'profile.html')


def edit_profile(request):
    if request.POST:
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        img = request.FILES.get('image')
        if not checking_name_email(request, email, name) and (email != request.user.email
                                                              or name != request.user.name):
            return redirect('user:edit_profile')

        request.user.name = name
        request.user.email = email
        request.user.phone = phone
        request.user.image = img
        request.user.about_me = request.POST.get('aboutMe')
        request.user.save()
        return redirect('user:profile')

    return render(request, 'edit_profile.html')

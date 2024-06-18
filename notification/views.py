# from django.shortcuts import render
# from .models import NotifyCargo, NotifyCar
# from car_cargo.models import Cargo, CarTypeBody, CarTypeLoading
# from car_cargo.views import VCar
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.utils import timezone
#
#
# # класс объекта уведомления
# class ObjectNotify:
#     def __init__(self, id, cargo=None, car=None):
#         self.cargo = cargo
#         self.car = car
#         self.id = id
#
#
# def objects_notify(cargs, cars):
#     objects = []
#     i = 0
#     j = 0
#     while i < len(cargs) and j < len(cars):
#         if cargs[i].id < cars[j].id:
#             obj = ObjectNotify(id=cars[j].id, car=cars[j])
#             objects.append(obj)
#             print(obj.id)
#             j += 1
#         else:
#             objects.append(ObjectNotify(id=cargs[i].id, cargo=cargs[i]))
#             i += 1
#
#     if i < len(cargs):
#         while i < len(cargs):
#             objects.append(ObjectNotify(id=cargs[i].id, cargo=cargs[i]))
#             i += 1
#     else:
#         while j < len(cars):
#             objects.append(ObjectNotify(id=cars[j].id, car=cars[j]))
#             j += 1
#
#     return objects
#
#
# def array_cars(cars):
#     array = []
#     today = timezone.now().date()
#     for i in cars:
#         if today > i.car.ready_from:
#             continue
#         car = VCar(_id=i.car.id, _name=i.car.car, _capacity=i.car.capacity, _volume=i.car.volume, _length=i.car.length,
#                    _width=i.car.width,
#                    _height=i.car.height, _where_from=i.car.where_from, _where=i.car.where, _ready_from=i.car.ready_from,
#                    _ready_to=i.car.ready_to,
#                    _phone=i.car.phone, _comment=i.car.comment)
#         types_body = CarTypeBody.objects.all().select_related('car', 'type_body')
#         check = False
#         j = 0
#         k = 0
#         while j < len(types_body):
#             if types_body[j].car.id == i.id:
#                 car.type_body.append(types_body[j].type_body.name)
#                 check = True
#             elif check:
#                 break
#             j += 1
#
#         check = False
#         types_loading = CarTypeLoading.objects.all().select_related('car', 'type_loading')
#         while k < len(types_loading):
#             if types_loading[k].car.id == i.id:
#                 car.type_loading.append(types_loading[k].type_loading.name)
#                 check = True
#             elif check:
#                 break
#             k += 1
#         array.append(car)
#
#     return array
#
#
# def array_cargs(cargs):
#     array = []
#     today = timezone.now().date()
#     for i in cargs:
#         cargo = Cargo.objects.get(id=i.cargo.id)
#         if cargo.loading_data >= today:
#             array.append(cargo)
#     return array
#
#
# def get_objects(notifications_cargo, notifications_car):
#     return objects_notify(array_cargs(notifications_cargo), array_cars(notifications_car))
#
#
# # функция которая возврщает словарб являющийся контекстом для страницы
# def get_context(notifications_cargo, notifications_car, request):
#     objects = get_objects(notifications_cargo, notifications_car)
#
#     for i in objects:
#         print(i.id)
#
#     paginator = Paginator(objects, per_page=4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'page_obj': page_obj
#     }
#     return context
#
#
# # функция которая передаст все мои уведомления на сайт
# def my_notification(request):
#     if request.POST:
#         if request.POST.get('obj_car_accept_id'):
#             obj_id = request.POST.get('obj_car_accept_id')
#             obj = NotifyCar.objects.get(id=obj_id)
#             obj.status_second_user = 'y'
#             obj.save()
#         elif request.POST.get('obj_car_reject_id'):
#             obj_id = request.POST.get('obj_car_reject_id')
#             obj = NotifyCar.objects.get(id=obj_id)
#             obj.status_second_user = 'n'
#             obj.save()
#         elif request.POST.get('obj_cargo_accept_id'):
#             obj_id = request.POST.get('obj_cargo_accept_id')
#             obj = NotifyCargo.objects.get(id=obj_id)
#             obj.status_second_user = 'y'
#             obj.save()
#         elif request.POST.get('obj_cargo_reject_id'):
#             obj_id = request.POST.get('obj_cargo_reject_id')
#             obj = NotifyCargo.objects.get(id=obj_id)
#             obj.status_second_user = 'n'
#             obj.save()
#
#     notifications_cargo = NotifyCargo.objects.all().filter(second_user=request.user).filter(
#         status_second_user='u').order_by("-id")
#     notifications_car = NotifyCar.objects.all().filter(second_user=request.user).filter(
#         status_second_user='u').order_by("-id")
#
#     context = get_context(notifications_cargo, notifications_car, request)
#     return render(request, 'MyNotification.html', context=context)
#
#
# # функция которая передаст все мои отклики на сайт
# def my_responses(request):
#     # удаление запроса
#     if request.POST:
#         if request.POST.get('obj_cargo_id'):
#             obj_id = request.POST.get('obj_cargo_id')
#             obj = NotifyCargo.objects.get(id=obj_id)
#             obj.delete()
#         else:
#             obj_id = request.POST.get('obj_car_id')
#             if NotifyCar.objects.get(id=obj_id) is not None:
#                 obj = NotifyCar.objects.get(id=obj_id)
#                 obj.delete()
#
#     notifications_cargo = NotifyCargo.objects.all().filter(first_user=request.user).order_by("-id")
#     notifications_car = NotifyCar.objects.all().filter(first_user=request.user).order_by("-id")
#     context = get_context(notifications_cargo, notifications_car, request)
#     return render(request, 'MyResponses.html', context=context)
#
#
# def match(request):
#     # достали все метчи
#     notifications_cargo = NotifyCargo.objects.all().filter(
#         Q(first_user=request.user) | Q(second_user=request.user)).filter(status_first_user='y').filter(
#         status_second_user='y')
#     notifications_car = NotifyCar.objects.all().filter(Q(first_user=request.user) | Q(second_user=request.user)).filter(
#         status_first_user='y').filter(status_second_user='y')
#
#     # получили контекст
#     context = get_context(notifications_cargo, notifications_car, request)
#     return render(request, 'Match.html', context=context)

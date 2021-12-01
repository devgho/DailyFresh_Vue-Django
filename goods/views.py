from django.shortcuts import render
from django.http import JsonResponse
from . import models


# Create your views here.


def get_goods(request):
    if request.GET.get('category', False):
        goods_list = list(models.Good.objects.filter(category__name=request.GET['category'])[:int(request.GET['limit'])].values())
    elif request.GET.get('id', False):
        goods_list = list(models.Good.objects.filter(id=request.GET['id']).values())
    elif request.GET.get('name', False):
        goods_list = list(models.Good.objects.filter(name__contains=request.GET['name']).values())
    else:
        goods_list = list(models.Good.objects.all()[:int(request.GET['limit'])].values())
    for i in goods_list:
        i['img'] = 'http://' + request.get_host() + '/media/' + i['img']
    return JsonResponse(goods_list, safe=False)


def get_types(request):
    type_list = list(models.Category.objects.all().values())
    return JsonResponse(type_list, safe=False)

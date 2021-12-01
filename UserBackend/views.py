from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models

from .models import User
# Create your views here.


def change(request):
    user = models.User.objects.filter(id=request.GET['user'])[0]
    user.address = request.GET['address']
    user.phone = request.GET['phone']
    user.receiver = request.GET['receiver']
    user.post_code = request.GET['post_code']
    user.save()
    return HttpResponse('success')


def get_user(request):
    user = list(models.User.objects.filter(id=request.GET['user']).values())
    return JsonResponse(user, safe=False)


def get_cart(request):
    user = models.User.objects.filter(id=request.GET['user'])[0]
    cart_list = []
    for i in user.cart_set.all():
        dic = {}
        dic['name'] = str(i.good.name)
        dic['sl'] = str(i.nums)
        dic['price'] = str(i.good.price)
        dic['image'] = 'http://' + request.get_host() + '/media/' + str(i.good.img)
        dic['id'] = str(i.id)
        cart_list.append(dic)
    return JsonResponse(cart_list, safe=False)


@csrf_exempt
def post_cart(request):
    cart = models.Cart()
    cart.user = models.User.objects.filter(id=request.GET['user_id'])[0]
    cart.good = models.Good.objects.filter(id=request.GET['good_id'])[0]
    cart.nums = request.GET['nums']
    cart.save()
    return HttpResponse('success')


@csrf_exempt
def delete_cart(request):
    cart = models.Cart(id=request.GET['id'])
    cart.delete()
    return HttpResponse('success')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            uname = request.POST['username']
            pwd = request.POST['password']
            password = models.User.objects.filter(username=uname)[0].password
            if pwd == password:
                return JsonResponse({'message': 'true', 'user': models.User.objects.filter(username=uname)[0].id}, safe=False)
            else:
                return JsonResponse({'message': 'false'})
        except IndexError:
            return JsonResponse({'message': 'none'})
    else:
        return HttpResponse('只允许POST')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.save()
        return JsonResponse({'message': 'true'})
    else:
        return HttpResponse('只允许POST')

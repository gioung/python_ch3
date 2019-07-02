from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')


def hello3(request):
    jsonresult = {
        'result': 'success',
        'data': ['hello', 1, 2, True, ('a', 'b', 'c')]

    }
    return JsonResponse(jsonresult)

def counter_update(request):
    # groupno = 1 이고 orderno >=2 의 게시물의 orderno 를 1씩증가
    # __gt, __lt, __gte, __lte
    list = Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno')+1)

    return HttpResponse('OK')

def counter_add(request):
    c = Counter()

    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()

    return HttpResponse('OK')

def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    return HttpResponse(f"max groupno:{value['max_groupno']}")



from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Hola la hora del servidor es {now}".format(now=now))


def hi(request):
    """hi"""
    numbers = (request.GET['numbers'])
    numbers = numbers.split(',')
    numbers = [int(elem) for elem in numbers]
    numbers.sort()
    return JsonResponse(numbers, safe=False)

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are to young'.format(name)
    else: 
        message = 'Hello {}, welcome to platzigram'.format(name)
    return HttpResponse(message)
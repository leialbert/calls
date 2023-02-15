from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.middleware import csrf
from django.http import HttpResponse
@csrf_exempt
def index(request):
    context = {}
    csrf_token = csrf.get_token(request)
    return HttpResponse(f'The CSRF token is: {csrf_token}')

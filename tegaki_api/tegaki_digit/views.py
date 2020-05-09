from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import JsonResponse


def index(request):
    res = {"content": "you are listening tegaki digit",}
    res = JsonResponse(res)
    res['Access-Control-Allow-Origin'] = "*"
    return res
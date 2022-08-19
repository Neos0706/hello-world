import time

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
import asyncio

def home1(request):
    time.sleep(15)
    return HttpResponse("我是阻塞同步视图")

async def home2(request):
    await asyncio.sleep(15)
    return HttpResponse("我是异步视图")

async def home3(request):
    return HttpResponse("我是异步视图home3")

def home4(request):
    return HttpResponse("我是同步视图home4")

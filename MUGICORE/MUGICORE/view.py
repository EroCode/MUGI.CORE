# -*- coding:utf-8 -*-

from django.shortcuts import render


def hello(request):
    context          = {}
    context["hello"] = "Mug.Wiki ------ 音游姬索引系统"
    return render(request, "hello.html", context)

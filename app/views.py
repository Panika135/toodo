from django.shortcuts import render,redirect
from django.views import View
from . import models
from django_tables2 import RequestConfig
from .filters import ToDoFilter
from .tables import *
from django import forms




class Home(View):
    def get(self, request):
        data = ToDo.objects.all()
        return render(request, 'home.html', {'data': data})



class Del(View):
    def post(self, request):
        avc = (list(request))
        print(avc)
        print((avc[0].decode('utf-8')))
        data = ToDo.objects.all()
        for i in data:
            try:
                request.POST[i.item]
            except Exception:
                i.checked = False
            else:
                i.checked = True
            finally:
                i.save()
        return redirect('/')


# def ToDo2(request):
#     my_filter = ToDoFilter(request.GET, queryset=models.ToDo.objects.all())
#     obj = my_filter.qs
#     table = ToDoTable(obj)
#     RequestConfig(request, paginate={"per_page": 25}).configure(table)
#     return render(request, 'test.html', {'table': table, 'myFilter': my_filter})


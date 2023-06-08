from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponseBadRequest
from flask import json
from django.views.decorators.csrf import csrf_exempt
from DJANGO_MVVM.dao_emp import DaoEmp

def index(request):
    return render(request, "index.html")

@csrf_exempt
def ajax(request):
    param = json.loads(request.body)
    print('param',param['menu'])
    #menu = request.GET.get('menu', '짜장면')
    context = {
        'menu' : param['menu']
    }
    
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_list(request):
    #param = json.loads(request.body)
    #print("fn_list실행")
    de = DaoEmp()
    emp_list = de.selectList();
    context = {
        'list' : emp_list
    }
    
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_detail(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    
    de = DaoEmp()
    vo = de.selectOne(e_id)
    
    context = {
        'vo' : vo
    }
    
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_update(request):
    param = json.loads(request.body)
    
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    
    context = {
        'cnt' : cnt
    }
    
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_insert(request):
    param = json.loads(request.body)
    
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, sex, addr)
    
    context = {
        'cnt' : cnt
    }
    
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_delete(request):
    param = json.loads(request.body)
    
    e_id = param['e_id']
    
    de = DaoEmp()
    cnt = de.delete(e_id)
    
    context = {
        'cnt' : cnt
    }
    
    return JsonResponse(context)

def todos(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            #todos = list(Todo.objects.all().values())
            return JsonResponse({'context': 'ajax 안녕!'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

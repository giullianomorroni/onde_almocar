#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from modelos.mongo import Mongo
import json
from modelos.restaurante import Restaurante

def _404(request):
    return '{"erro":"serviço não existe", "codigo":404}';

def _500(request):
    return '{"erro":"erro inesperado", "codigo":500}';

@csrf_exempt
def teste(request):
    return HttpResponse('test ok' + str(request))

@csrf_exempt
def autenticar(request):
    json_data = request.POST['json']
    json_data = json.loads(json_data)
    email = json_data['email']
    mongo = Mongo()
    r = mongo.pesquisar_cliente_por_email(email)
    r = json.dumps(r)
    return HttpResponse('result' + r)

@csrf_exempt
def pesquisar_locais(request):
    json_data = request.POST['json']
    filtro = json.loads(json_data)
    mongo = Mongo()
    r = mongo.pesquisar_locais(filtro)
    r = json.dumps(r)

    restaurantes = []
    for aux in r:
        r = Restaurante();
        r.extrair_classe(aux);
        restaurantes.append(r);

    return HttpResponse('result' + r)

@csrf_exempt
def inserir_local(request):
    json_data = request.POST['json']
    local = json.loads(json_data)
    mongo = Mongo()
    r = mongo.inserir_local(local);
    r = json.dumps(r)
    return HttpResponse('result' + r)

@csrf_exempt
def favoritar(request):
    json_data = request.POST['json']
    local = json.loads(json_data)
    mongo = Mongo()
    r = mongo.inserir_favorito(local);
    r = json.dumps(r)
    return HttpResponse('result' + r)

@csrf_exempt
def inserir_perfil_cliente(request):
    json_data = request.POST['json']
    json_data = json.loads(json_data)
    mongo = Mongo()
    r = mongo.inserir_perfil_cliente(json_data)
    r = json.dumps(r)
    return HttpResponse('result' + r)

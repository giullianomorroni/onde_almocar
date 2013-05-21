#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from modelos.mongo import Mongo
import json

def _404(request):
    return '{"erro":"serviço não existe", "codigo":404}';

def _500(request):
    return '{"erro":"erro inesperado", "codigo":500}';

@csrf_exempt
def autenticar(request):
    json_data = request.POST['json']
    json_data = json.loads(json_data)
    email = json_data['email']
    print email
    mongo = Mongo()
    r = mongo.pesquisar_cliente_por_email(email)
    print r
    r = json.dumps(r)
    return HttpResponse('result' + r)

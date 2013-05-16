#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext

def _404(request):
    return '{"erro":"serviço não existe", "codigo":404}';

def _500(request):
    return '{"erro":"erro inesperado", "codigo":500}';

def autenticar(request):
    json = request.POST['json']
    
    return json 


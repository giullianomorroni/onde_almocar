# -*- coding: utf-8 -*-
import json

class Endereco():

    global logradouro
    global numero
    global complemento
    global cep
    global bairro
    global cidade
    global estado

    def __init__(self):
        self.logradouro = ''
        self.numero = ''
        self.complemento = ''
        self.cep = 0
        self.bairro = ''
        self.cidade = ''
        self.estado = ''

    def extrair_classe(self, json_data):
        aux = json.loads(json_data)
        self.logradouro = aux['logradouro']
        self.numero = aux['numero']
        self.complemento = aux['complemento']
        self.cep = aux['cep']
        self.bairro = aux['bairro']
        self.cidade = aux['cidade']
        self.estado = aux['estado']
        return self

    def extrair_json(self):
        js_dt = json.dumps(
        {
        	"logradouro" : self.logradouro, 
        	"numero" : self.numero,
        	"complemento" : self.complemento,
        	"cep" : self.cep,
        	"bairro" : self.bairro,
        	"cidade" : self.cidade,
        	"estado" : self.estado
        }, ensure_ascii=False
        )
        return json.loads(js_dt)
# -*- coding: utf-8 -*-
import json

class PerfilRestaurante():

    global preco_medio
    global conforto
    global barulho
    global categoria
    global tipo
    global espaco_proprio
 
    def __init__(self):
        self.preco_medio = 0.0
        self.conforto = 0
        self.barulho = 0
        self.categoria = ''
        self.tipo = ''
        self.espaco_proprio = False

    def extrair_classe(self, json_data):
        aux = json.loads(json_data)
        self.preco_medio = aux['preco_medio'];
        self.conforto = aux['conforto'];
        self.barulho = aux['barulho'];
        self.categoria = aux['categoria'];
        self.tipo = aux['tipo'];
        self.espaco_proprio = aux['espaco_proprio'];
        return self

    def extrair_json(self):
        js_dt = json.dumps(
          {
    	"preco_medio" : self.preco_medio, 
    	"barulho" : self.barulho, 
    	"conforto" : self.conforto,
    	"categoria" : self.categoria,
    	"tipo" : self.tipo,
    	"espaco_proprio" : self.espaco_proprio
          },
          ensure_ascii=False
        )
        return json.loads(js_dt)
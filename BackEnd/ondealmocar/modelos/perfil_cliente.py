# -*- coding: utf-8 -*-
import json

class PerfilCliente():

    global preco_medio
    global conforto
    global barulho
    
    global ordenar_distancia
    global ordenar_barulho
    global ordenar_conforto
    global ordenar_preco_medio
    
    global somente_favorito
    global somente_primeira_vez
    global somente_espaco_proprio
    
    #não persistir esses valores...
    global latitude
    global longitude

    def __init__(self):
        self.preco_medio = 0.0
        self.conforto = 0
        self.barulho = 0
        self.ordenar_distancia = False
        self.ordenar_barulho = False
        self.ordenar_conforto = False
        self.ordenar_preco_medio = False
        self.somente_favorito = False
        self.somente_primeira_vez = False
        self.somente_espaco_proprio = False
        self.latitude = None
        self.longitude = None

    def extrair_classe(self, json_data):
        aux = json.loads(json_data)
        self.preco_medio = aux['preco_medio'];
        self.conforto = aux['conforto'];
        self.barulho = aux['barulho'];
        return self

    def extrair_json(self):
        js_dt = json.dumps(
        {
        	"preco_medio":self.preco_medio, 
        	"barulho":self.barulho, 
        	"conforto": self.conforto
        }, ensure_ascii=False
        )
        return json.loads(js_dt)
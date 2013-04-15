# -*- coding: utf-8 -*-
import json

class PerfilCliente():

  global preco_medio
  global conforto
  global barulho

  def __init__(self):
    self.preco_medio = 0.0
    self.conforto = 0
    self.barulho = 0

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
      }
    )
    return js_dt
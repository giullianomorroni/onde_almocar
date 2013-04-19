# -*- coding: utf-8 -*-
import json

class Caracteristica():

  global distancia
  global primeira_vez
  global favorito

  def __init__(self):
    self.distancia = 0.0
    self.primeira_vez = False
    self.favorito = False

  def extrair_classe(self, json_data):
    aux = json.loads(json_data)
    self.distancia = aux['distancia'];
    self.primeira_vez = aux['primeira_vez'];
    self.favorito = aux['favorito'];
    return self

  def extrair_json(self):
    js_dt = json.dumps(
      {
	"distancia":self.distancia, 
	"primeira_vez":self.primeira_vez, 
	"favorito": self.favorito
      },
      ensure_ascii=False
    )
    return json.loads(js_dt)
package br.com.ondealmocar;

import java.math.BigDecimal;

import org.json.JSONException;
import org.json.JSONObject;

public class Filtro implements ConversorJson {
	
  private List<String> tipos;
  private Boolean salaoProprio;
  private String quantPessoas;
  private List<String> favoritos;
  private Boolean buscaExata;
  private Double latitude;
  private Double longitude;
  
  
  public String json() {
		JSONObject jsonObject = new JSONObject();
		try {
		  jsonObject.put("tipos", this.tipos);
		  jsonObject.put("quant_pessoas", this.quantPessoas);
		  jsonObject.put("favoritos", this.favoritos);
		  jsonObject.put("busca_exata", this.buscaExata);
		  jsonObject.put("latitude", this.latitude);
		  jsonObject.put("longitude", this.longitude);
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return jsonObject.toString();
	}

	public void entidade(String json) {
		try {
			JSONObject jsonObject = new JSONObject(json);
			this.precoMedio = new BigDecimal(jsonObject.optDouble("preco_medio"));
			//TODO TERMINAR....
		} catch (JSONException e) {
			e.printStackTrace();
		}

	}
  }
package br.com.ondealmocar;

import java.math.BigDecimal;

import org.json.JSONException;
import org.json.JSONObject;

public class PerfilRestaurante implements ConversorJson {

	private String id;
	private BigDecimal precoMedio;
	private Integer conforto;
	private Integer barulho;
	private String categoria;
	private String tipo;
	private Boolean espacoProprio;

	public String json() {
		JSONObject jsonObject = new JSONObject();
		try {
			jsonObject.put("id", this.id);
			jsonObject.put("preco_medio", this.precoMedio);
			jsonObject.put("conforto", this.conforto);
			jsonObject.put("barulho", this.barulho);
			jsonObject.put("categoria", this.categoria);
			jsonObject.put("tipo", this.tipo);
			jsonObject.put("espaco_proprio", this.espacoProprio);
		} catch (JSONException e) {
			e.printStackTrace();
		}

		return jsonObject.toString(); 
	}

	public void entidade(String json) {
		try {
			JSONObject jsonObject = new JSONObject(json);
	
			this.id = jsonObject.optString("id");
			this.precoMedio = new BigDecimal(jsonObject.optDouble("preco_medio"));
			this.conforto = jsonObject.optInt("conforto");
			this.barulho = jsonObject.optInt("barulho");
			this.categoria = jsonObject.optString("categoria");
			this.tipo = jsonObject.optString("tipo");
			this.espacoProprio = jsonObject.optBoolean("espaco_proprio");		
		} catch (JSONException e) {
			e.printStackTrace();
		}
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public BigDecimal getPrecoMedio() {
		return precoMedio;
	}

	public void setPrecoMedio(BigDecimal precoMedio) {
		this.precoMedio = precoMedio;
	}

	public Integer getConforto() {
		return conforto;
	}

	public void setConforto(Integer conforto) {
		this.conforto = conforto;
	}

	public Integer getBarulho() {
		return barulho;
	}

	public void setBarulho(Integer barulho) {
		this.barulho = barulho;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public Boolean getEspacoProprio() {
		return espacoProprio;
	}

	public void setEspacoProprio(Boolean espacoProprio) {
		this.espacoProprio = espacoProprio;
	}

}

package br.com.ondealmocar;

import org.json.JSONObject;

public class Caracteristica implements ConversorJson {

	private String id;
	private Double distancia;
	private Boolean primeiraVez;
	private Boolean favorito;

	@Override
	public String json() {
		JSONObject jsonObject = new JSONObject();

		jsonObject.put("id", this.id);
		jsonObject.put("distancia", this.distancia);
		jsonObject.put("primeira_vez", this.primeiraVez);
		jsonObject.put("favorito", this.favorito);

		return jsonObject.toString();
	}

	@Override
	public void entidade(String json) {
		JSONObject jsonObject = new JSONObject(json);
		this.id = jsonObject.optString("id");
		this.distancia = jsonObject.optDouble("distancia");
		this.primeiraVez = jsonObject.optBoolean("primeira_vez");
		this.favorito = jsonObject.optBoolean("favorito");
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Double getDistancia() {
		return distancia;
	}

	public void setDistancia(Double distancia) {
		this.distancia = distancia;
	}

	public Boolean getPrimeiraVez() {
		return primeiraVez;
	}

	public void setPrimeiraVez(Boolean primeiraVez) {
		this.primeiraVez = primeiraVez;
	}

	public Boolean getFavorito() {
		return favorito;
	}

	public void setFavorito(Boolean favorito) {
		this.favorito = favorito;
	}

}

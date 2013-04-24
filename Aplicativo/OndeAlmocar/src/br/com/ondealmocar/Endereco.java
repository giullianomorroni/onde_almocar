package br.com.ondealmocar;

import org.json.JSONException;
import org.json.JSONObject;

public class Endereco implements ConversorJson {

	private String id;
	private String logradouro;
	private String numero;
	private String complemento;
	private String cep;
	private Double latitude;
	private Double longitude;
	private String bairro;
	private String cidade;
	private String estado;

	public String json() {
		JSONObject jsonObject = new JSONObject();
		try {
			jsonObject.put("id", this.id);
			jsonObject.put("logradouro", this.logradouro);
			jsonObject.put("numero", this.numero);
			jsonObject.put("complemento", this.complemento);
			jsonObject.put("cep", this.cep);
			jsonObject.put("latitude", this.latitude);
			jsonObject.put("longitude", this.longitude);
			jsonObject.put("bairro", this.bairro);
			jsonObject.put("cidade", this.cidade);
			jsonObject.put("estado", this.estado);
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return jsonObject.toString(); 
	}

	public void entidade(String json) {
		try {
			JSONObject jsonObject = new JSONObject(json);
	
			this.id = jsonObject.optString("id");
			this.logradouro = jsonObject.optString("logradouro");
			this.numero = jsonObject.optString("numero");
			this.complemento = jsonObject.optString("complemento");
			this.cep = jsonObject.optString("cep");
			this.latitude = jsonObject.optDouble("latitude");
			this.longitude = jsonObject.optDouble("longitude");
			this.bairro = jsonObject.optString("bairro");
			this.cidade = jsonObject.optString("cidade");
			this.estado = jsonObject.optString("estado");
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

	public String getLogradouro() {
		return logradouro;
	}

	public void setLogradouro(String logradouro) {
		this.logradouro = logradouro;
	}

	public String getNumero() {
		return numero;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}

	public String getComplemento() {
		return complemento;
	}

	public void setComplemento(String complemento) {
		this.complemento = complemento;
	}

	public String getCep() {
		return cep;
	}

	public void setCep(String cep) {
		this.cep = cep;
	}

	public Double getLatitude() {
		return latitude;
	}

	public void setLatitude(Double latitude) {
		this.latitude = latitude;
	}

	public Double getLongitude() {
		return longitude;
	}

	public void setLongitude(Double longitude) {
		this.longitude = longitude;
	}

	public String getBairro() {
		return bairro;
	}

	public void setBairro(String bairro) {
		this.bairro = bairro;
	}

	public String getCidade() {
		return cidade;
	}

	public void setCidade(String cidade) {
		this.cidade = cidade;
	}

	public String getEstado() {
		return estado;
	}

	public void setEstado(String estado) {
		this.estado = estado;
	}

}

package br.com.ondealmocar;

import java.math.BigDecimal;

import org.json.JSONException;
import org.json.JSONObject;

public class PerfilCliente implements ConversorJson {

	private String id;
	private BigDecimal precoMedio;
	private Integer conforto;
	private Integer barulho;

	private Boolean ordenarDistancia;
	private Boolean ordenarBarulho;
	private Boolean ordenarConforto;
	private Boolean ordenarPrecoMedio;

	private Boolean somenteFavorito;
	private Boolean somentePrimeiraVez;
	private Boolean somenteEspacoProprio;

	public String json() {
		JSONObject jsonObject = new JSONObject();
		try {
			jsonObject.put("id", this.id);
			jsonObject.put("preco_medio", this.precoMedio);
			jsonObject.put("conforto", this.conforto);
			jsonObject.put("barulho", this.barulho);
			
			jsonObject.put("ordenar_distancia", this.ordenarDistancia);
			jsonObject.put("ordenar_barulho", this.ordenarBarulho);
			jsonObject.put("ordenar_conforto", this.ordenarConforto);
			jsonObject.put("ordenar_preco_medio", this.ordenarPrecoMedio);
			jsonObject.put("somente_favorito", this.somenteFavorito);
			jsonObject.put("somente_primeira_vez", this.somentePrimeiraVez);
			jsonObject.put("somente_espaco_proprio", this.somenteEspacoProprio);
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
	
			this.ordenarDistancia = jsonObject.optBoolean("ordenar_distancia");
			this.ordenarBarulho = jsonObject.optBoolean("ordenar_barulho");
			this.ordenarConforto = jsonObject.optBoolean("ordenar_conforto");
			this.ordenarPrecoMedio = jsonObject.optBoolean("ordenar_preco_medio");
			this.somenteFavorito = jsonObject.optBoolean("somente_favorito");
			this.somentePrimeiraVez = jsonObject.optBoolean("somente_primeira_vez");
			this.somenteEspacoProprio = jsonObject.optBoolean("somente_espaco_proprio");
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

	public Boolean getOrdenarDistancia() {
		return ordenarDistancia;
	}

	public void setOrdenarDistancia(Boolean ordenarDistancia) {
		this.ordenarDistancia = ordenarDistancia;
	}

	public Boolean getOrdenarBarulho() {
		return ordenarBarulho;
	}

	public void setOrdenarBarulho(Boolean ordenarBarulho) {
		this.ordenarBarulho = ordenarBarulho;
	}

	public Boolean getOrdenarConforto() {
		return ordenarConforto;
	}

	public void setOrdenarConforto(Boolean ordenarConforto) {
		this.ordenarConforto = ordenarConforto;
	}

	public Boolean getOrdenarPrecoMedio() {
		return ordenarPrecoMedio;
	}

	public void setOrdenarPrecoMedio(Boolean ordenarPrecoMedio) {
		this.ordenarPrecoMedio = ordenarPrecoMedio;
	}

	public Boolean getSomenteFavorito() {
		return somenteFavorito;
	}

	public void setSomenteFavorito(Boolean somenteFavorito) {
		this.somenteFavorito = somenteFavorito;
	}

	public Boolean getSomentePrimeiraVez() {
		return somentePrimeiraVez;
	}

	public void setSomentePrimeiraVez(Boolean somentePrimeiraVez) {
		this.somentePrimeiraVez = somentePrimeiraVez;
	}

	public Boolean getSomenteEspacoProprio() {
		return somenteEspacoProprio;
	}

	public void setSomenteEspacoProprio(Boolean somenteEspacoProprio) {
		this.somenteEspacoProprio = somenteEspacoProprio;
	}

}

package com.ondealmocar.dominio;

import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Cliente implements ConversorJson {

	private String id;
	private String nome;
	private String email;
	private PerfilCliente perfil;
	private List<Estabelecimento> almocos = new ArrayList<Estabelecimento>();
	private List<Cliente> amigos = new ArrayList<Cliente>();
	private List<Estabelecimento> favoritos = new ArrayList<Estabelecimento>();

	public String json() {
		JSONObject jsonObject = new JSONObject();
		try {
	
			jsonObject.put("id", this.id);
			jsonObject.put("nome", this.nome);
			jsonObject.put("emai", this.email);
			jsonObject.put("perfil_cliente", this.perfil);
	
			JSONArray jsonArray = new JSONArray();
			for (Estabelecimento restaurante : almocos)
				jsonArray.put(restaurante.json());
			jsonObject.put("almocos", jsonArray);
	
			jsonArray = new JSONArray();
			for (Cliente cliente : amigos)
				jsonArray.put(cliente.json());
			jsonObject.put("amigos", jsonArray);
	
			jsonArray = new JSONArray();
			for (Estabelecimento restaurante : favoritos)
				jsonArray.put(restaurante.json());
			jsonObject.put("favoritos", jsonArray);
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return jsonObject.toString();
	}

	public void entidade(String json) {
		try{
			
			JSONObject jsonObject = new JSONObject(json);
	
			this.id = jsonObject.optString("id");
			this.nome = jsonObject.optString("nome");
			this.email = jsonObject.optString("emai");
			JSONObject jsonPerfil = jsonObject.optJSONObject("perfil_cliente");
			if (jsonPerfil != null) {
				this.perfil = new PerfilCliente();
				this.perfil.entidade(jsonPerfil.toString());
			}
	
			JSONArray jsonArrayAlmocos = jsonObject.optJSONArray("almocos");
			for (int i=0; i < jsonArrayAlmocos.length(); i++) {
				JSONObject jsonAlmoco = jsonArrayAlmocos.getJSONObject(i);
				Estabelecimento restaurante = new Estabelecimento();
				restaurante.entidade(jsonAlmoco.toString());
				this.almocos.add(restaurante);
			}
	
			JSONArray jsonArrayFavoritos = jsonObject.optJSONArray("favoritos");
			for (int i=0; i < jsonArrayFavoritos.length(); i++) {
				JSONObject jsonFavorito = jsonArrayFavoritos.getJSONObject(i);
				Estabelecimento restaurante = new Estabelecimento();
				restaurante.entidade(jsonFavorito.toString());
				this.favoritos.add(restaurante);
			}
	
			JSONArray jsonArrayAmigos = jsonObject.optJSONArray("amigos");
			for (int i=0; i < jsonArrayAmigos.length(); i++) {
				JSONObject jsonFavorito = jsonArrayAmigos.getJSONObject(i);
				Cliente cliente = new Cliente();
				cliente.entidade(jsonFavorito.toString());
				this.amigos.add(cliente);
			}
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

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public PerfilCliente getPerfil() {
		return perfil;
	}

	public void setPerfil(PerfilCliente perfil) {
		this.perfil = perfil;
	}

	public List<Estabelecimento> getAlmocos() {
		return almocos;
	}

	public void setAlmocos(List<Estabelecimento> almocos) {
		this.almocos = almocos;
	}

	public List<Cliente> getAmigos() {
		return amigos;
	}

	public void setAmigos(List<Cliente> amigos) {
		this.amigos = amigos;
	}

	public List<Estabelecimento> getFavoritos() {
		return favoritos;
	}

	public void setFavoritos(List<Estabelecimento> favoritos) {
		this.favoritos = favoritos;
	}

}

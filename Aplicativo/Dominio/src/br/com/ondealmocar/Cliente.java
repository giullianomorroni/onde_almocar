package br.com.ondealmocar;

import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONObject;

public class Cliente implements ConversorJson {

	private String id;
	private String nome;
	private String email;
	private PerfilCliente perfil;
	private List<Restaurante> almocos = new ArrayList<>();
	private List<Cliente> amigos = new ArrayList<>();
	private List<Restaurante> favoritos = new ArrayList<>();

	@Override
	public String json() {
		JSONObject jsonObject = new JSONObject();

		jsonObject.put("id", this.id);
		jsonObject.put("nome", this.nome);
		jsonObject.put("emai", this.email);
		jsonObject.put("perfil_cliente", this.perfil);

		JSONArray jsonArray = new JSONArray();
		for (Restaurante restaurante : almocos)
			jsonArray.put(restaurante.json());
		jsonObject.put("almocos", jsonArray);

		jsonArray = new JSONArray();
		for (Cliente cliente : amigos)
			jsonArray.put(cliente.json());
		jsonObject.put("amigos", jsonArray);

		jsonArray = new JSONArray();
		for (Restaurante restaurante : favoritos)
			jsonArray.put(restaurante.json());
		jsonObject.put("favoritos", jsonArray);

		return jsonObject.toString();
	}

	@Override
	public void entidade(String json) {
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
			Restaurante restaurante = new Restaurante();
			restaurante.entidade(jsonAlmoco.toString());
			this.almocos.add(restaurante);
		}

		JSONArray jsonArrayFavoritos = jsonObject.optJSONArray("favoritos");
		for (int i=0; i < jsonArrayFavoritos.length(); i++) {
			JSONObject jsonFavorito = jsonArrayFavoritos.getJSONObject(i);
			Restaurante restaurante = new Restaurante();
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

	public List<Restaurante> getAlmocos() {
		return almocos;
	}

	public void setAlmocos(List<Restaurante> almocos) {
		this.almocos = almocos;
	}

	public List<Cliente> getAmigos() {
		return amigos;
	}

	public void setAmigos(List<Cliente> amigos) {
		this.amigos = amigos;
	}

	public List<Restaurante> getFavoritos() {
		return favoritos;
	}

	public void setFavoritos(List<Restaurante> favoritos) {
		this.favoritos = favoritos;
	}

}
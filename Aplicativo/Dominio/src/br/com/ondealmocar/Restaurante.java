package br.com.ondealmocar;

import org.json.JSONObject;

public class Restaurante implements ConversorJson {

	private String id;
	private String nome;
	private String site;
	private String email;
	private String telefone;
	private String horario;
	private String descricao;
	private Endereco endereco;
	private PerfilRestaurante perfil;
	private Caracteristica caracteristica;
	private Double pontuacao;

	@Override
	public String json() {
		JSONObject jsonObject = new JSONObject();

		jsonObject.put("id", this.id);
		jsonObject.put("nome", this.nome);
		jsonObject.put("site", this.site);
		jsonObject.put("email", this.email);
		jsonObject.put("telefone", this.telefone);
		jsonObject.put("horario", this.horario);
		jsonObject.put("descricao", this.descricao);
		jsonObject.put("pontuacao", this.pontuacao);

		if (this.perfil != null)
			jsonObject.put("perfil_restaurante", this.perfil.json());

		if (this.caracteristica != null)
			jsonObject.put("caracteristica", this.caracteristica.json());

		if (this.endereco != null)
			jsonObject.put("endereco", this.endereco.json());

		return jsonObject.toString();
	}

	@Override
	public void entidade(String json) {
		JSONObject jsonObject = new JSONObject(json);

		this.id = jsonObject.optString("id");
		this.nome = jsonObject.optString("nome");
		this.site = jsonObject.optString("site");
		this.email = jsonObject.optString("email");
		this.telefone = jsonObject.optString("telefone");
		this.horario = jsonObject.optString("horario");
		this.descricao = jsonObject.optString("descricao");
		this.pontuacao = jsonObject.optDouble("pontuacao");

		JSONObject jsonPerfil = jsonObject.optJSONObject("perfil_restaurante");
		this.perfil = new PerfilRestaurante();
		if (jsonPerfil != null)
			this.perfil.entidade(jsonPerfil.toString());

		JSONObject jsonCaracteristica = jsonObject.optJSONObject("caracteristica ");
		this.caracteristica = new Caracteristica();
		if (jsonCaracteristica != null)
			this.caracteristica.entidade(jsonCaracteristica.toString());	

		JSONObject jsonEndereco = jsonObject.optJSONObject("endereco");
		this.endereco = new Endereco();
		if (jsonEndereco != null)
			this.endereco.entidade(jsonEndereco.toString());

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

	public String getSite() {
		return site;
	}

	public void setSite(String site) {
		this.site = site;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getTelefone() {
		return telefone;
	}

	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}

	public String getHorario() {
		return horario;
	}

	public void setHorario(String horario) {
		this.horario = horario;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public Endereco getEndereco() {
		return endereco;
	}

	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}

	public PerfilRestaurante getPerfil() {
		return perfil;
	}

	public void setPerfil(PerfilRestaurante perfil) {
		this.perfil = perfil;
	}

	public Caracteristica getCaracteristica() {
		return caracteristica;
	}

	public void setCaracteristica(Caracteristica caracteristica) {
		this.caracteristica = caracteristica;
	}

	public Double getPontuacao() {
		return pontuacao;
	}

	public void setPontuacao(Double pontuacao) {
		this.pontuacao = pontuacao;
	}

}

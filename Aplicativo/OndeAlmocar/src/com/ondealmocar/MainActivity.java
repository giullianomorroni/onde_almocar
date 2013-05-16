package com.ondealmocar;

import android.app.Activity;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.WindowManager;
import android.widget.TextView;

import com.ondealmocar.dominio.Cliente;

public class MainActivity extends Activity {

	private static String email;

	@Override
    public void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState);
		StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
		StrictMode.setThreadPolicy(policy);
		setContentView(R.layout.authenticate_screen);
		getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_ALWAYS_HIDDEN);
    }

    @Override
	public boolean onCreateOptionsMenu(Menu menu) {
		MenuInflater inflater = getMenuInflater();
	    inflater.inflate(R.menu.activity_main, menu);
	    return true;
	}
    
    @Override
	public boolean onOptionsItemSelected(MenuItem item) {
	    switch (item.getItemId()) {
	        case R.id.tela_principal:
	            setContentView(R.layout.main_screen);
	            return true;
	        default:
	            return super.onOptionsItemSelected(item);
	    }
	}

    public void registrarEstabelecimento(View view) {
    	
    }

    public void registrarCliente(View view) {
//    	EditText inputNome = (EditText) findViewById(R.id.editText_contato_nome);
//		EditText inputTelefone = (EditText) findViewById(R.id.editText_contato_telefone);
//		Spinner spinerOperadora = (Spinner) findViewById(R.id.spinner_contato_operadoras);
//
//		String nome = String.valueOf(inputNome.getText());
//		String operadora = String.valueOf(spinerOperadora.getSelectedItem());
//		String numero = String.valueOf(inputTelefone.getText());
//
//		if (numero != null && numero.length() > 0) {
//			Telefone telefone = new Telefone(numero, operadora);
//			novosTelefones.add(telefone);
//		}
//		Contato usuario = new Contato(this.id, nome, novosTelefones, "");
//		registrarContato(usuario);
    }

    public void meuPerfil(View view) {
    	setContentView(R.layout.client_profile);
    }

    public void telaPrincipal(View view) {
    	setContentView(R.layout.main_screen);
    }

    public void favoritos(View view) {
    	setContentView(R.layout.favorite_screen);
    }

    public void iniciarPesquisa(View view) {
    	setContentView(R.layout.establishment_filter_screen);
    }

    public void novoRestaurante(View view) {
    	setContentView(R.layout.establishment_screen);
    }

    public void autenticar(View view) {
    	TextView viewEmail = (TextView) findViewById(R.id.email);
    	CharSequence text = viewEmail.getText();
    	email = String.valueOf(text);
    	setContentView(R.layout.main_screen);
    }

    public void passo2(View view) {
    	setContentView(R.layout.establishment_profile_screen);
    }
    
    public void passo3(View view) {
    	setContentView(R.layout.establishment_address_screen);
    }
    
    public void cadastrarRestaurante(View view) {
    	setContentView(R.layout.main_screen);
    }
    
    private void registrarCliente(Cliente cliente) {
//    	try {
//			HttpClient client = new RestFul().createHttpClient();
//			HttpPost post = new HttpPost(URL.REGISTRAR_CONTATO.getValor(PRODUCAO));
//			HttpParams httpParameters = new BasicHttpParams();
//			HttpProtocolParams.setContentCharset(httpParameters, "utf-8");
//			post.setParams(httpParameters);
//
//			List<NameValuePair> pairs = new ArrayList<NameValuePair>();
//			pairs.add(new BasicNameValuePair("json", contato.gerarJson()));
//			post.setEntity(new UrlEncodedFormEntity(pairs));
//			client.execute(post);
//			setContentView(R.layout.activity_filtro);
//		} catch (ClientProtocolException e) {
//			Toast.makeText(MainActivity.this, "Telefone inválido",Toast.LENGTH_LONG).show();
//		} catch (IOException e) {
//			Toast.makeText(MainActivity.this, "Telefone inválido",Toast.LENGTH_LONG).show();
//		}
    }

}

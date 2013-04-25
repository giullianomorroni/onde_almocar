package com.ondealmocar;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;

public class MainActivity extends Activity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState);
		StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
		StrictMode.setThreadPolicy(policy);
		setContentView(R.layout.activity_main);
		//EditText emailInput = (EditText) findViewById(R.id.editText_email);
		//EditText pinInput = (EditText) findViewById(R.id.editText_pin);
		//emailInput.setText("giullianomorroni@gmail.com");
		//pinInput.setText("123456");
		//manter o teclado fechado...
		getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_ALWAYS_HIDDEN);
        setContentView(R.layout.activity_main);
    }

    @Override
	public boolean onCreateOptionsMenu(Menu menu) {
		MenuInflater inflater = getMenuInflater();
	    inflater.inflate(R.menu.activity_main, menu);
	    return true;
	}
    
    @Override
	public boolean onOptionsItemSelected(MenuItem item) {
//	    switch (item.getItemId()) {
//	        case R.id.menu_sincronizar:
//	            sincronizarContatos(item.getActionView());
//	            return true;
//	        default:
//	            return super.onOptionsItemSelected(item);
//	    }
    	return true;
	}
    
    public void registrarEstabelecimento(View view) {
    	
    }

    public void registrarCliente(View view) {
    	EditText inputNome = (EditText) findViewById(R.id.editText_contato_nome);
		//EditText inputDDD = (EditText) findViewById(R.id.editText_contato_ddd);
		EditText inputTelefone = (EditText) findViewById(R.id.editText_contato_telefone);
		Spinner spinerOperadora = (Spinner) findViewById(R.id.spinner_contato_operadoras);

		String nome = String.valueOf(inputNome.getText());
		String operadora = String.valueOf(spinerOperadora.getSelectedItem());
		String numero = String.valueOf(inputTelefone.getText());

		if (numero != null && numero.length() > 0) {
			Telefone telefone = new Telefone(numero, operadora);
			novosTelefones.add(telefone);
		}
		Contato usuario = new Contato(this.id, nome, novosTelefones, "");
		registrarContato(usuario);
    }
    
    private void registrarCliente(Cliente cliente) {
    	try {
			HttpClient client = new RestFul().createHttpClient();
			HttpPost post = new HttpPost(URL.REGISTRAR_CONTATO.getValor(PRODUCAO));
			HttpParams httpParameters = new BasicHttpParams();
			HttpProtocolParams.setContentCharset(httpParameters, "utf-8");
			post.setParams(httpParameters);

			List<NameValuePair> pairs = new ArrayList<NameValuePair>();
			pairs.add(new BasicNameValuePair("json", contato.gerarJson()));
			post.setEntity(new UrlEncodedFormEntity(pairs));
			client.execute(post);
			setContentView(R.layout.activity_filtro);
		} catch (ClientProtocolException e) {
			Toast.makeText(MainActivity.this, "Telefone inválido",Toast.LENGTH_LONG).show();
		} catch (IOException e) {
			Toast.makeText(MainActivity.this, "Telefone inválido",Toast.LENGTH_LONG).show();
		}
    }

    public void pesquisarEstabelecimento(View view) {
    	
    }

    private void pesquisarEstabelecimento(Caracteristica caracteristica, Cliente cliente) {
    	
    }

}

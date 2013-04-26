package com.ondealmocar;

import java.util.ArrayList;
import java.util.List;

import com.ondealmocar.dominio.Caracteristica;
import com.ondealmocar.dominio.Cliente;
import com.ondealmocar.listener.SlidingDrawerListener;

import android.app.Activity;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.WindowManager;
import android.widget.SlidingDrawer;

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

    public void autenticar(View view) {
    	setContentView(R.layout.tela_pesquisa);
    	
    	SlidingDrawer slidingDrawerQualidade = (SlidingDrawer) findViewById(R.id.slidingDrawerQualidade);
		SlidingDrawer slidingDrawerPrecoMedio = (SlidingDrawer) findViewById(R.id.slidingDrawerPrecoMedio);
		SlidingDrawer slidingDrawerQtdPessoa = (SlidingDrawer) findViewById(R.id.slidingDrawerQuantPessoas);
		SlidingDrawer slidingDrawerSalao = (SlidingDrawer) findViewById(R.id.slidingDrawerSalaoProprio);
		SlidingDrawer slidingDrawerTipos = (SlidingDrawer) findViewById(R.id.slidingDrawerTipos);

		List<SlidingDrawer> slidings = new ArrayList<SlidingDrawer>();
		slidings.add(slidingDrawerQualidade);
		slidings.add(slidingDrawerPrecoMedio);
		slidings.add(slidingDrawerQtdPessoa);
		slidings.add(slidingDrawerSalao);
		slidings.add(slidingDrawerTipos);
		
		SlidingDrawerListener drawerListener = new SlidingDrawerListener(slidings);
		slidingDrawerQualidade.setOnClickListener(drawerListener);
		slidingDrawerPrecoMedio.setOnClickListener(drawerListener);
		slidingDrawerQtdPessoa.setOnClickListener(drawerListener);
		slidingDrawerSalao.setOnClickListener(drawerListener);
		slidingDrawerTipos.setOnClickListener(drawerListener);

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

    public void pesquisarEstabelecimento(View view) {
    	
    }

    private void pesquisarEstabelecimento(Caracteristica caracteristica, Cliente cliente) {
    	
    }

}

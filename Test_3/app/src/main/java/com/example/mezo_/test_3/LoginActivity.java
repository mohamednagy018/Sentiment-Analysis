package com.example.mezo_.test_3;

import android.content.Context;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;

public class LoginActivity extends AppCompatActivity {
    Button loginBTN;
    EditText usernameField;
    EditText passwordField;
    @Override

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        loginBTN = (Button) findViewById(R.id.loginBTN);
        usernameField  = (EditText) findViewById(R.id.email);
        passwordField  = (EditText) findViewById(R.id.pass);

        loginBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String username = usernameField.getText().toString();
                String password = passwordField.getText().toString();
                new loginDb(getApplicationContext()).execute(username,password);
            }
        });

    }
    public class loginDb extends AsyncTask<String,String ,String>{

        Context co;
        public loginDb(Context c)
        {
            this.co = c;
        }

        @Override
        protected String doInBackground(String... arg0) {
            try{
                Log.e("EEEEEEEEEEEEE","EEEEEEEEEEE");
                String username = arg0[0];
                String password = arg0[1];
                Log.e("EEEEEEEEEEEEE",password);

                String link = "https://gpwebfunction.000webhostapp.com/login.php?username="+username+"&password="+password+"";
                URL url = new URL(link);
                HttpClient client = new DefaultHttpClient();
                HttpGet request = new HttpGet();
                request.setURI(new URI(link));
                HttpResponse response = client.execute(request);
                BufferedReader in = new BufferedReader(new
                        InputStreamReader(response.getEntity().getContent()));
                Log.e("EEEEEEEEEEEEE",in.toString());
                StringBuffer sb = new StringBuffer("");
                String line="";


                while ((line = in.readLine()) != null) {
                    Log.e("EEEEEEEEEEEEEvvvv",line);

                    sb.append(line);
                }

                in.close();
                return sb.toString();
            } catch(Exception e){
                return "Exception: " + e.getMessage();
            }
        }
    }



}


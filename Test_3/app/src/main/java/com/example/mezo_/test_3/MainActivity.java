package com.example.mezo_.test_3;

import android.app.Activity;
import android.graphics.Typeface;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Window;
import android.widget.GridView;
import android.widget.LinearLayout;
import android.widget.TabHost;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView t;

 @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        this.requestWindowFeature(Window.FEATURE_NO_TITLE);

        setContentView(R.layout.activity_main);
        t= (TextView) findViewById(R.id.RegisterAkhbari);
        Typeface myCustomFont= Typeface.createFromAsset(getAssets(),"fonts/Dosis-ExtraBold.ttf");
        t.setTypeface(myCustomFont);



    }


}

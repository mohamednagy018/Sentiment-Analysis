package com.example.mezo_.test_3;

import android.graphics.Typeface;
import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Window;
import android.widget.TabHost;
import android.widget.TextView;


public class Welcome1 extends Fragment
{
    TextView t;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,Bundle     savedInstanceState) {
        View v = inflater.inflate(R.layout.welcome1_screen, container, false);
        TextView txt = (TextView) v.findViewById(R.id.welcometitle);
        Typeface font = Typeface.createFromAsset(getActivity().getAssets(), "fonts/Dosis-ExtraBold.ttf");
        txt.setTypeface(font);
        return v;
    }

}

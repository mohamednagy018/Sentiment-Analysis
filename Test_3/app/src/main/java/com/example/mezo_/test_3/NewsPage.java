package com.example.mezo_.test_3;

import android.content.Context;
import android.graphics.Color;
import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.GridLayout;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

/**
 * Created by mezo_ on 9/7/2017.
 */

public class NewsPage extends Fragment {

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater,  ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.news_screen, container, false);

        LinearLayout linear = (LinearLayout) v.findViewById(R.id.NewsScreen);
        GridLayout gridLayout;

// Add Title

       // param.setGravity(Gravity.CENTER);
       // param.columnSpec = GridLayout.spec(1);
      //  param.rowSpec = GridLayout.spec(1);
        TextView tv1, tv2;
        Button b1,b2;
        EditText et;
        for (int i = 0; i<10 ; i++) {
            gridLayout = new GridLayout(getContext());
            gridLayout.setColumnCount(4);
            gridLayout.setRowCount(6);

            gridLayout.setBackgroundColor(Color.parseColor("#E4E4E4"));
            gridLayout.setPadding(8,6,8,6);

            GridLayout.LayoutParams param =new GridLayout.LayoutParams();

            param.height = GridLayout.LayoutParams.WRAP_CONTENT;
            param.width = GridLayout.LayoutParams.WRAP_CONTENT;
             tv1 = new TextView(getContext());
            tv1.setText("Published on:");
            tv1.setPadding(15, 0, 0, 0);

            tv1.setTextColor(Color.parseColor("#ffffff"));
            tv1.setBackgroundColor(getResources().getColor(R.color.colorAccent));

            // param.columnSpec = GridLayout.spec(0);
            //param.rowSpec = GridLayout.spec(0);
            //tv1.setLayoutParams (param);
            tv1.setTextSize(25);
            gridLayout.addView(tv1, new GridLayout.LayoutParams(
                    GridLayout.spec(0, 1),
                    GridLayout.spec(0, 4, GridLayout.FILL)));


             tv2 = new TextView(getContext());
            tv2.setText("Post Post Post PostPost Post Post Post Post Post Post Post Post Post Post Post Post Post Post Post Post Post PostPostPost Post");
            tv2.setTextColor(getResources().getColor(R.color.colorAccent));

            // param.columnSpec = GridLayout.spec(0);
            //  param.rowSpec = GridLayout.spec(1);
            //  tv2.setLayoutParams (param);
            tv2.setTextSize(18);
            gridLayout.addView(tv2, new GridLayout.LayoutParams(
                    GridLayout.spec(1, 1),
                    GridLayout.spec(0, 4)));

             b2 = new Button(getContext());
            b2.setText("Follow");
            // param.columnSpec = GridLayout.spec(0);
            //  param.rowSpec = GridLayout.spec(2);
            // b2.setLayoutParams (param);
            b2.setTextColor(Color.parseColor("#ffffff"));
            b2.setBackgroundColor(getResources().getColor(R.color.colorAccent));

            gridLayout.addView(b2, new GridLayout.LayoutParams(
                    GridLayout.spec(2, 1),
                    GridLayout.spec(0, 1)));


             b1 = new Button(getContext());
            b1.setText("Sentement");
            // param.columnSpec = GridLayout.spec(1);
            //  param.rowSpec = GridLayout.spec(2);
            //  b1.setLayoutParams (param);
            b1.setTextColor(Color.parseColor("#ffffff"));
            b1.setBackgroundColor(getResources().getColor(R.color.colorAccent));

            gridLayout.addView(b1, new GridLayout.LayoutParams(
                    GridLayout.spec(2, 1),
                    GridLayout.spec(3, 1)));

             et = new EditText(getContext());
            et.setHint("Comment");
            et.setBackgroundColor(Color.parseColor("#ffffff"));
            gridLayout.addView(et, new GridLayout.LayoutParams(
                    GridLayout.spec(3, 2),
                    GridLayout.spec(0, 4, GridLayout.FILL)));

            linear.addView(gridLayout);

        }
        return v;
    }


}

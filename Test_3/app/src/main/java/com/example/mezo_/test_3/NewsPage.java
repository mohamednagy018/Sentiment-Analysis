package com.example.mezo_.test_3;

import android.content.Context;
import android.graphics.Color;
import android.graphics.Typeface;
import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
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

import java.util.ArrayList;
import java.util.List;

/**
 * Created by mezo_ on 9/7/2017.
 */

public class NewsPage extends Fragment {
    private RecyclerView rv;
    private rvAdapter adapter;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater,  ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.news_screen, container, false);
        rv = (RecyclerView) v.findViewById(R.id.NewsScreen);
        adapter = new rvAdapter(getActivity(),getData());
        rv.setAdapter(adapter);

        rv.setLayoutManager(new LinearLayoutManager(getActivity(), LinearLayoutManager.VERTICAL,false));
        rv.setNestedScrollingEnabled(false);

        return v;
    }
    public static List<rvData> getData(){
        List<rvData> data = new ArrayList<>();
        int[] icons= {R.drawable.day7,R.drawable.day7,R.drawable.day7,R.drawable.day7};
        String[] titles= {"اليوم السابع","سي.ان.ان","اليوم السابع","BBC"};
        String[] bodies= {"دخول شاب من المعادي في غيبوبة مفاجئة بعد اكله لشيبسي بالشطة والليمون وشربه لكان بيريل."
                ,"محاولة انتحار بائسة لشاب من سكان المعادي بعد فقدانه لاحد صوابع البقسماط خاصته."
                ,"tiitle1title1title1itle1title1title1itle1title1title1itle1title1title1itle1title1title1itle1title1title1itle1title1title13te3"
                ,"itlitle1title1title1itle1title1title1itle1title1title1itle1title1title1itle1title1title1itle1title1title1itle1title1title1e4"};
        for (int i=0;i<titles.length;i++){
            rvData current = new rvData();
            current.titleid= titles[i];
            current.postbodyid= bodies[i];
            current.imgid=icons[i];
            data.add(current);
        }
    return data;
    }


}

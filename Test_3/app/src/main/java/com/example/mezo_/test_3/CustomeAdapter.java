package com.example.mezo_.test_3;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;

/**
 * Created by mezo_ on 9/27/2017.
 */

public class CustomeAdapter extends BaseAdapter {
    private String[ ] imageLabels;
    private Context context;
    private LayoutInflater thisInflater;
    public CustomeAdapter( Context con, String[ ] labs ) {
        this.context = con;
        this.thisInflater = LayoutInflater.from(con);
        this.imageLabels = labs;
    }

    @Override
    public int getCount() {
        return pets.length;
    }

    @Override
    public Object getItem(int position) {
        return position;
    }

    @Override
    public long getItemId(int position) {
        return position;

    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        return null;
    }

  public Integer[] pets ={
          R.drawable.web_hi_res_512
  };

}

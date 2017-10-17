package com.example.mezo_.test_3;

import android.content.Context;
import android.content.Intent;
import android.graphics.Typeface;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.Collections;
import java.util.List;

import static android.support.v4.content.ContextCompat.startActivity;

/**
 * Created by mezo_ on 9/30/2017.
 */

public class rvAdapter extends RecyclerView.Adapter<rvAdapter.MyViewHolder> {

    private  LayoutInflater inflater;
    List<rvData> data= Collections.emptyList();
    public rvAdapter(Context context, List<rvData> data){
        inflater=LayoutInflater.from(context);
        this.data=data;
    }
    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view=inflater.inflate(R.layout.custome_post, parent,false);

        MyViewHolder holder = new MyViewHolder(view);

        return holder;
    }

    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {
        rvData current = data.get(position);
        holder.title.setText(current.titleid);
        holder.postbody.setText(current.postbodyid);
        holder.titleimg.setImageResource(current.imgid);
    }

    @Override
    public int getItemCount() {

        return data.size();
    }

    class  MyViewHolder extends RecyclerView.ViewHolder {
        TextView title,postbody;
        ImageView titleimg;

        public MyViewHolder(final View itemView) {
            super(itemView);

            title= itemView.findViewById(R.id.title);
            postbody= itemView.findViewById(R.id.postbody);
            titleimg= itemView.findViewById(R.id.titleimg);
            Typeface tf_regular = Typeface.createFromAsset(itemView.getContext().getAssets(), "fonts/NeoSansArabic.ttf");
            Typeface tf_regular2 = Typeface.createFromAsset(itemView.getContext().getAssets(), "fonts/DIN-NEXT_-ARABIC-REGULAR.otf");
            this.title.setTypeface(tf_regular);
            this.postbody.setTypeface(tf_regular2);

            Button btn = (Button)itemView.findViewById(R.id.fulldetailsBTN);
            TextView txt = (TextView) itemView.findViewById(R.id.postbody);
            final Intent intent = new Intent(itemView.getContext(), PostDetailActivity.class);
            btn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    v.getContext().startActivity(intent);
                }
            });
            txt.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    v.getContext().startActivity(intent);
                }
            });
        }
    }
}

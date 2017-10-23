package com.example.mezo_.test_3;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by mezo_ on 9/7/2017.
 */

public class NewsPage extends Fragment  {

    private RecyclerView rv;
    private rvAdapter adapter;
    public static ArrayList<String> Descriptions = new ArrayList<>();
    public static List<rvData> data = new ArrayList<>();
    public static int[] icons = {R.drawable.day7, R.drawable.day7, R.drawable.day7, R.drawable.day7, R.drawable.day7};
    public static String[] titles = {"اليوم السابع", "سي.ان.ان", "اليوم السابع", "BBC", "CNN"};

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        final View v = inflater.inflate(R.layout.news_screen, container, false);
        JSONTask asyncTask = (JSONTask) new JSONTask(new JSONTask.AsyncResponse(){


            @Override
            public void processFinish(ArrayList<String> output) {
                Descriptions = output;
                rv = (RecyclerView) v.findViewById(R.id.NewsScreen);
                adapter = new rvAdapter(getActivity(), getData());
                rv.setAdapter(adapter);

                rv.setLayoutManager(new LinearLayoutManager(getActivity(), LinearLayoutManager.VERTICAL, false));
                rv.setNestedScrollingEnabled(false);

            }
        }).execute("http://192.168.1.2:8000/stocks/?format=json");

        return v;
    }

    public List<rvData> getData() {
        for (int i = 0; i < Descriptions.size(); i++) {
            rvData current = new rvData();
            current.titleid = titles[0];
            current.postbodyid = Descriptions.get(i);
            current.imgid = icons[0];
            data.add(current);
        }
        return data;
    }





    public static class JSONTask extends AsyncTask<String, String, ArrayList<String>> {
        public interface AsyncResponse {
            void processFinish(ArrayList<String> output);
        }

        public AsyncResponse delegate = null;

        public JSONTask(AsyncResponse delegate){
            this.delegate = delegate;
        }
        @Override
        protected ArrayList<String> doInBackground(String... params) {
            HttpURLConnection connection = null;
            BufferedReader reader = null;
            ArrayList<String> bodies = new ArrayList<>();
            try {
                URL url = new URL(params[0]);
                connection = (HttpURLConnection) url.openConnection();
                connection.connect();
                InputStream stream = connection.getInputStream();
                if (stream.available() == 1) {
                    Log.e("EEEEEEEEEee", "EEEEEEEe");

                } else {
                    Log.e("FFFFFFFFFF", stream.available() + "");
                }
                reader = new BufferedReader(new InputStreamReader(stream));
                StringBuffer buffer = new StringBuffer();

                String line = "";
                int x = 0;
                while ((line = reader.readLine()) != null) {
                    buffer.append(line);
                    x++;
                    Log.e("DDDDDDDDDDDDDDDDDDdd", line);
                    Log.e("DDDDDDDDDDDDDDDDDDdd", x + "");
                }
                String josn_s = buffer.toString();
                Log.e("SSSSSSSSSSSs", josn_s);

                // ...
                JSONArray json = new JSONArray(josn_s);
// ...

                for (int i = 0; i < json.length(); i++) {
                    JSONObject e = json.getJSONObject(i);
                    Log.e("F", e.getString("summary_news"));
                    bodies.add(e.getString("summary_news"));
                }
                return bodies;
            } catch (IOException e) {
                Log.e("DDDDDDDDDDDD", e.getMessage());

            } catch (JSONException e) {
                e.printStackTrace();
            }

            return null;
        }

        @Override
        protected void onPostExecute(ArrayList<String> result) {
            super.onPostExecute(result);
            //Log.e("DDDDDDDDDDDDDD",result);
            delegate.processFinish(result);

        }

    }

}

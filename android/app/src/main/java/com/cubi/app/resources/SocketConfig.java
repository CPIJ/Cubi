package com.cubi.app.resources;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;

public class SocketConfig {

    private final static String configLocation = "com/cubi/app/resources/server-config.json";
    private final static String json = readAllText(configLocation);

    public static Config getConfig(String serverName) {
        Config config = null;

        try {
            JSONObject obj = new JSONObject(json);
            JSONObject obj2 = obj.getJSONObject(serverName);

            config = new Config(obj2.getString("host"), obj2.getInt("port"));

        } catch (JSONException e) {
            e.printStackTrace();
        }

        return config;
    }

    private static String readAllText(String file)  {

        StringBuilder sb = new StringBuilder(512);
        FileInputStream is = null;
        try {
            is = new FileInputStream(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        try {
            Reader r = new InputStreamReader(is, "UTF-8");
            int c = 0;
            while ((c = r.read()) != -1) {
                sb.append((char) c);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return sb.toString();
    }
}

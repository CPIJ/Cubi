package com.cubi.app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {


    private String message_IO = "";
    private String message_Logic = "";
    private Socket_Client socket_io;
    private Socket_Client socket_logic;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        socket_io = new Socket_Client("192.168.70.146", 8002);
        socket_logic = new Socket_Client("192.168.70.57", 8001);
    }

}

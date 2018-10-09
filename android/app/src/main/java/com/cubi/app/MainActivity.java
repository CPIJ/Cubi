package com.cubi.app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;


import com.cubi.app.Communication.Socket_Client;
import com.cubi.app.resources.Config;
import com.cubi.app.resources.SocketConfig;

import java.net.Socket;

public class MainActivity extends AppCompatActivity {
    private String socket_IO_Address = "192.168.70.146";
    private String socket_Logic_Address = "192.168.70.57";
    private int socket_IO_Port = 8002;
    private int socket_Logic_Port = 8001;

    private Socket_Client Client_io;
    private Socket_Client Client_logic;
    private Socket socket_IO = null;
    private Socket socket_logic = null;
   // private Config CONFIG_LOGIC = SocketConfig.getConfig("LOGIC_SERVER");
   // private Config CONFIG_IO = SocketConfig.getConfig("IO_SERVER");

    TextView response;
    EditText editTextAddress, editTextPort;
    Button buttonConnect, buttonTraining, buttonConversation, buttonLevel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        buttonConnect = findViewById(R.id.connectButton);
        buttonTraining =  findViewById(R.id.trainingButton);
        buttonConversation = findViewById(R.id.conversationButton);
        response = findViewById(R.id.responseTextView);
        buttonLevel = findViewById(R.id.levelButton);

        buttonConnect.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View arg0) {
                Client_io = new Socket_Client(socket_IO,socket_IO_Address, socket_IO_Port);
                Client_io.setMessage("SET_MODE:STANDBY");
                Client_io.execute();

            }
        });

        buttonTraining.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Client_io = new Socket_Client(socket_IO,socket_IO_Address, socket_IO_Port);

                Client_io.setMessage("SET_MODE:TRAINING");
                Client_io.execute();
            }
        });

              buttonConversation.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
              //  Client_io = new Socket_Client(socket_IO,CONFIG_IO.getHost(), CONFIG_IO.getPort());
                Client_io = new Socket_Client(socket_IO,socket_IO_Address, socket_IO_Port);

                Client_io.setMessage("SET_MODE:CONVERSATION");
                Client_io.execute();
            }
        });

        buttonLevel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Client_logic = new Socket_Client(socket_logic, LOGIC_CONFIG.getHost(), LOGIC_CONFIG.getPort());

               // Client_logic.setMessage("SET_LEVEL:2");
                //Client_logic.execute();
            }
        });

        buttonLevel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
              //  Client_logic = new Socket_Client(socket_logic, CONFIG_LOGIC.getHost(), CONFIG_LOGIC.getPort());
                Client_logic = new Socket_Client(socket_IO,socket_Logic_Address, socket_Logic_Port);

                Client_logic.setMessage("TOGGLE_EMOTION:HAPPY");
                Client_logic.execute();
            }
        });

    }
}
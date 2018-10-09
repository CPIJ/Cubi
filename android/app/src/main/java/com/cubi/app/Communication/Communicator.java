package com.cubi.app.Communication;

import android.app.Activity;
import android.os.Bundle;

import java.net.Socket;

public class Communicator extends Activity {

    public static Application application;
    private String socket_IO_Address = "192.168.250.2";
    private String socket_Logic_Address = "192.168.250.1";
    private int socket_IO_Port = 8002;
    private int socket_Logic_Port = 8001;
    private int socket_Server = 8003;

    private Socket_Client Client_io;
    private Socket_Client Client_logic;
    private Socket socket_IO = null;
    private Socket socket_logic = null;
    private Socket socket_server = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    public void control_IO (String message)
    {
        Client_io = new Socket_Client(socket_IO,socket_IO_Address, socket_IO_Port);
        Client_io.setMessage(message);
        Client_io.execute();
    }

    public void control_logic (String message)
    {
        Client_logic = new Socket_Client(socket_logic, socket_Logic_Address, socket_Logic_Port);
        Client_logic.setMessage("TOGGLE_EMOTION:HAPPY");
        Client_logic.execute();
    }

}

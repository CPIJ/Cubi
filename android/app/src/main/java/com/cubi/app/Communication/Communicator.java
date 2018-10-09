package com.cubi.app.Communication;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class Communicator extends Activity {

    public static Application application;

    
    private String socket_IO_Address = "192.168.250.2";
    private String socket_Logic_Address = "192.168.250.3";
    private int socket_IO_Port = 8002;
    private int socket_Logic_Port = 8001;
   // private int socket_Server = 8003;

    private Socket_IO_Client Client_io;
    private Socket_logic_Client Client_logic;
    private Socket socket_IO = null;
    private Socket socket_logic = null;
    //private Socket socket_server = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    public void control_IO (String message)
    {
        Client_io = new Socket_IO_Client();
        Client_io.setMessage(message);
        Client_io.execute();
    }

    public void control_logic (String message)
    {
        Client_logic = new Socket_logic_Client();
        Client_logic.setMessage(message);
        Client_logic.execute();
    }

    public class Socket_logic_Client extends AsyncTask<Void, Void, Void> {
        private String message = "";
        private PrintWriter printWriter = null;

        public void setMessage(String message)
        {
            this.message = message;
        }

        @Override
        protected Void doInBackground(Void... voids) {
            try {
                if (socket_logic == null) {
                    socket_logic = new Socket(socket_Logic_Address, socket_Logic_Port);
                }

                if (printWriter == null) {
                    printWriter = new PrintWriter(socket_logic.getOutputStream());
                }

                printWriter.write(message);
                printWriter.flush();

            }
            catch (UnknownHostException e)
            {
                e.printStackTrace();

            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return null;
        }
    }

    public class Socket_IO_Client extends AsyncTask<Void, Void, Void> {
        private String message = "";
        private PrintWriter printWriter = null;

        public void setMessage(String message)
        {
            this.message = message;
        }

        @Override
        protected Void doInBackground(Void... voids) {
            try {
                if (socket_IO == null) {
                    socket_IO = new Socket(socket_IO_Address, socket_IO_Port);
                }

                if (printWriter == null) {
                    printWriter = new PrintWriter(socket_IO.getOutputStream());
                }

                printWriter.write(message);
                printWriter.flush();

            }
            catch (UnknownHostException e)
            {
                e.printStackTrace();

            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return null;
        }
    }
}

package com.cubi.app;

import android.os.AsyncTask;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;

public class Socket_Client extends AsyncTask<Void, Void, Void> {

    private String  IP_Address;
    private int port;
    private String message = "";
    private Socket socket = null;
    private PrintWriter printWriter= null;

    public void setMessage(String message)
    {
        this.message = message;
    }

    public Socket_Client( String  IP_Address, int port)
    {
        this.IP_Address = IP_Address;
        this.port = port;
    }

    @Override
    protected Void doInBackground(Void... voids) {

        try {
            if (socket == null) {
                socket = new Socket(IP_Address, port);

            }

            if (printWriter == null) {
                printWriter = new PrintWriter(socket.getOutputStream());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        printWriter.write(message);
        printWriter.flush();
        return null;
    }
}

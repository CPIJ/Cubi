package com.cubi.app.Communication;

import android.os.AsyncTask;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class Socket_Client extends AsyncTask<Void, Void, Void> {

    private String  IP_Address;
    private int port;
    private String message = "";
    private Socket socket = null;
    private PrintWriter printWriter = null;

    public void setMessage(String message)
    {
        this.message = message;
    }

    public Socket_Client(Socket socket, String  IP_Address, int port)
    {
        this.socket = socket;
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

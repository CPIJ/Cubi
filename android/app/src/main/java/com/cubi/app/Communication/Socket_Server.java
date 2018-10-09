package com.cubi.app.Communication;

import android.os.AsyncTask;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;

public class Socket_Server extends AsyncTask<Void, Void, Void> {

    private String  IP_Address;
    private int port;
    private String message = "";
    private ServerSocket serverSocket = null;
    private PrintWriter printWriter = null;
    private int count = 0;

    public void setMessage(String message)
    {
        this.message = message;
    }

    public Socket_Server(ServerSocket socket, String  IP_Address, int port)
    {
        this.serverSocket = socket;
        this.IP_Address = IP_Address;
        this.port = port;
    }

    @Override
    protected Void doInBackground(Void... voids) {
        try {
            if (serverSocket == null) {
                serverSocket = new ServerSocket(port);
            }

            while (true)
            {
                Socket socket = serverSocket.accept();
                count++;
                message += "#" + count + " from "
                        + socket.getInetAddress() + ":"
                        + socket.getPort() + "\n";
            }


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

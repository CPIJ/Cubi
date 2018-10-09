package com.cubi.app.Communication;

import java.io.IOException;
import java.net.Socket;

public class Application extends android.app.Application {

    public static Application application;
    public static Communicator communicator;

   // private String socket_IO_Address = "192.168.250.2";
   // private String socket_Logic_Address = "192.168.250.1";
    //private int socket_IO_Port = 8002;
   // private int socket_Logic_Port = 8001;

   // private Socket_Client Client_io;
   // private Socket_Client Client_logic;
  //  private Socket socket_IO = null;
   // private Socket socket_logic = null;

    @Override
    public void onCreate() {
        super.onCreate();
        communicator = new Communicator();
        application = this;
    }

    @Override
    public void onTerminate() {
        super.onTerminate();
        /*
        try
        {
            Application.application.control_IO("SET_MODE:STANDBY");
            //socket_IO.close();
            //socket_logic.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        */
    }
}

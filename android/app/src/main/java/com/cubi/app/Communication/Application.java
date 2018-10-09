package com.cubi.app.Communication;

import com.cubi.app.Cubi;



public class Application extends android.app.Application {

    public static Application application;
    public static Communicator communicator;
    public static Cubi cubi;


    @Override
    public void onCreate() {
        super.onCreate();
        communicator = new Communicator();
        cubi = new Cubi();
        application = this;
    }

    @Override
    public void onTerminate() {
        super.onTerminate();
        communicator.CloseSockets();
    }
}

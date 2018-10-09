package com.cubi.app;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;

import com.cubi.app.Communication.Application;

/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 */
public class LoadingScreen extends AppCompatActivity {

    private final int LOADING_SCREEN_DELAY = 3000;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading_screen);


        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                //Application.application.control_IO("SET_MODE:STANDBY");
                startActivity(new Intent(LoadingScreen.this, ModusScreen.class));
                finish();
            }
        }, LOADING_SCREEN_DELAY);
    }
}

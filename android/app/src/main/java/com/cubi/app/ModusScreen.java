package com.cubi.app;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.cubi.app.Communication.Application;
import com.cubi.app.Communication.Communicator;
import com.cubi.app.Communication.Socket_Client;
import com.cubi.app.Conversation.ConversationActivity;
import com.cubi.app.Training.TrainingActivity;

public class ModusScreen extends AppCompatActivity {

    Button button_training_modus, button_gespreks_modus;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_modus_screen);

        button_training_modus = findViewById(R.id.button_trainingsmodus);
        button_gespreks_modus = findViewById(R.id.button_gespreksmodus);

        button_training_modus.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View arg0) {
               // Application.application.control_IO("SET_MODE:STANDBY");
                Application.communicator.control_IO("SET_MODE:TRAINING");
                //Application.application.control_IO("SET_MODE:TRAINING");
                //communicator.control_IO("SET_MODE:TRAINING");
                startActivity(new Intent(ModusScreen.this, TrainingActivity.class));
            }
        });

        button_gespreks_modus.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                //Application.application.control_IO("SET_MODE:STANDBY");
                //communicator.control_IO("SET_MODE:CONVERSATION");
                Application.communicator.control_IO("SET_MODE:CONVERSATION");
                //Application.application.control_IO("SET_MODE:CONVERSATION");
                startActivity(new Intent(ModusScreen.this, ConversationActivity.class));
            }
        });
    }
}



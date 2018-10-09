package com.cubi.app.Training;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

import com.cubi.app.Communication.Application;
import com.cubi.app.R;

public class TrainingActivity extends AppCompatActivity {

    Button button_stop_training;
    ImageButton button_happy, button_angry, button_surprise, button_sad;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_training);

        button_stop_training = findViewById(R.id.button_stop_trainingmodus);
        button_happy = findViewById(R.id.button_toggle_training_happy);
        button_angry = findViewById(R.id.button_toggle_training_angry);
       // button_surprise = findViewById(R.id.button_toggle_surprise);
        button_sad = findViewById(R.id.button_toggle_training_sad);

        button_stop_training.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
               // Application.application.control_IO("SET_MODE:STANDBY");
                finish();
            }
        });

        button_happy.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                // Application.application.control_IO("SET_MODE:STANDBY");
                Application.communicator.control_logic("TOGGLE_EMOTION:HAPPY");
            }
        });

        button_angry.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                // Application.application.control_IO("SET_MODE:STANDBY");
                Application.communicator.control_logic("TOGGLE_EMOTION:ANGRY");
            }
        });

        button_sad.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                // Application.application.control_IO("SET_MODE:STANDBY");
                Application.communicator.control_logic("TOGGLE_EMOTION:SAD");
            }
        });
    }
}

package com.cubi.app.Training;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.cubi.app.Communication.Application;
import com.cubi.app.R;

public class TrainingActivity extends AppCompatActivity {

    Button button_stop_training;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_training);

        button_stop_training = findViewById(R.id.button_stop_trainingmodus);

        button_stop_training.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
               // Application.application.control_IO("SET_MODE:STANDBY");
                finish();
            }
        });
    }
}

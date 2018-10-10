package com.cubi.app.Training;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

import com.cubi.app.Communication.Application;
import com.cubi.app.R;

public class TrainingActivity extends AppCompatActivity {

    Button button_stop_training;
    ImageButton button_happy, button_angry, button_surprise, button_sad, button_fear, button_disgust;
    TextView textView_niveau;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_training);

        button_stop_training = findViewById(R.id.button_stop_trainingmodus);
        button_happy = findViewById(R.id.button_toggle_training_happy);
        button_angry = findViewById(R.id.button_toggle_training_angry);
        button_surprise = findViewById(R.id.button_toggle_training_surprise);
        button_sad = findViewById(R.id.button_toggle_training_sad);
        button_fear = findViewById(R.id.button_toggle_training_fear);
        button_disgust = findViewById(R.id.button_toggle_training_disgust);
        textView_niveau = findViewById(R.id.textView_training_niveau);

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
                Application.cubi.ToggleEmotionBlacklisted("HAPPY");
                updateUI();
            }
        });

        button_angry.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Application.cubi.ToggleEmotionBlacklisted("ANGRY");
                updateUI();
            }
        });

        button_sad.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Application.cubi.ToggleEmotionBlacklisted("SAD");
                updateUI();

            }
        });

        button_fear.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Application.cubi.ToggleEmotionBlacklisted("FEAR");
                updateUI();
            }
        });

        button_disgust.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Application.cubi.ToggleEmotionBlacklisted("DISGUST");
                updateUI();
            }
        });
        updateUI();
    }

    private void updateUI()
    {
        if(Application.cubi.findEmotion("HAPPY").isBlacklisted())
        {
            button_happy.setImageResource(R.drawable.ic_visibility);
        }
        else button_happy.setImageResource(R.color.green);

        if(Application.cubi.findEmotion("ANGRY").isBlacklisted()) {
            button_angry.setImageResource(R.drawable.ic_visibility);
        }
        else button_angry.setImageResource(R.color.red);

        if(Application.cubi.findEmotion("SURPRISE").isBlacklisted())
        {
            button_surprise.setImageResource(R.drawable.ic_visibility);
        }
        else button_surprise.setImageResource(R.color.pink);

        if(Application.cubi.findEmotion("SAD").isBlacklisted())
        {
            button_sad.setImageResource(R.drawable.ic_visibility);
        }
        else button_sad.setImageResource(R.color.blueEmotie);

        if(Application.cubi.findEmotion("FEAR").isBlacklisted())
        {
            button_fear.setImageResource(R.drawable.ic_visibility);
        }
        else button_fear.setImageResource(R.color.yellow);

        if(Application.cubi.findEmotion("DISGUST").isBlacklisted())
        {
            button_disgust.setImageResource(R.drawable.ic_visibility);
        }
        else button_disgust.setImageResource(R.color.orange);
        updateNiveau();
    }

    private void updateNiveau()
    {
        int niveau = Application.cubi.getNiveau();
        if(niveau == 1)
        {
            textView_niveau.setText("Standaard");
        }
        else if (niveau == 2)
        {
            textView_niveau.setText("Alleen positief en negatief");
        }

        else if (niveau == 3)
        {
            textView_niveau.setText("Er wordt een emotie getoond maar Cubi zal niet laten zien welke Emotie getoond wordt");
        }
    }
}

package com.cubi.app.Conversation;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

import com.cubi.app.Communication.Application;
import com.cubi.app.Communication.Socket_Client;
import com.cubi.app.LoadingScreen;
import com.cubi.app.ModusScreen;
import com.cubi.app.R;

public class ConversationActivity extends AppCompatActivity {

    Button button_stop_conversation, button_settings;
    ImageButton button_happy, button_anger, button_surprise, button_sad, button_fear, button_disgust;

    private void updateUI()
    {
        if(Application.cubi.findEmotion("HAPPY").isBlacklisted())
        {
            button_happy. = false;
        }

        if(Application.cubi.findEmotion("ANGRY").isBlacklisted())
        {
            //button_anger
        }

        if(Application.cubi.findEmotion("SURPRISE").isBlacklisted())
        {
        }

        if(Application.cubi.findEmotion("SAD").isBlacklisted())
        {
        }

        if(Application.cubi.findEmotion("FEAR").isBlacklisted())
        {
        }

        if(Application.cubi.findEmotion("DISGUST").isBlacklisted())
        {

        }

    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_conversation);
        button_stop_conversation = findViewById(R.id.button_stop_gespreksmodus);
        button_settings = findViewById(R.id.button_Instellingen);
        button_happy = findViewById(R.id.button_toggle_happy);
        button_anger = findViewById(R.id.button_toggle_angry);
        button_surprise = findViewById(R.id.button_toggle_surprise);
        button_sad = findViewById(R.id.button_toggle_sad);
        button_fear = findViewById(R.id.button_toggle_fear);
        button_disgust = findViewById(R.id.button_toggle_disgust);

        updateUI();


        button_stop_conversation.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                //Application.application.control_IO("SET_MODE:STANDBY");
                finish();
            }
        });

        button_settings.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                //Application.application.control_IO("SET_MODE:STANDBY");
                startActivity(new Intent(ConversationActivity.this, ConversationSettingsActivity.class));
            }
        });

        button_happy.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
               //Application.application.control_logic("TOGGLE_EMOTION:HAPPY");
              // Application.communicator.control_logic("TOGGLE_EMOTION:HAPPY");
               Application.cubi.ToggleEmotionBlacklisted("HAPPY");

            }
        });

        button_anger.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                //Application.communicator.control_logic("TOGGLE_EMOTION:ANGRY");
                Application.cubi.ToggleEmotionBlacklisted("ANGRY");
            }
        });

        button_surprise.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Application.cubi.ToggleEmotionBlacklisted("SURPRISE");
               // Application.communicator.control_logic("TOGGLE_EMOTION:SURPRISE");
            }
        });

        button_sad.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
               // Application.communicator.control_logic("TOGGLE_EMOTION:SAD");
                Application.cubi.ToggleEmotionBlacklisted("SAD");
            }
        });

        button_fear.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                //Application.communicator.control_logic("TOGGLE_EMOTION:FEAR");
                Application.cubi.ToggleEmotionBlacklisted("FEAR");
            }
        });

        button_disgust.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                //Application.communicator.control_logic("TOGGLE_EMOTION:DISGUST");
                Application.cubi.ToggleEmotionBlacklisted("DISGUST");
            }
        });
    }
}

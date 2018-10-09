package com.cubi.app.Conversation;

import android.content.Intent;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

import com.cubi.app.Communication.Application;
import com.cubi.app.R;

public class ConversationActivity extends AppCompatActivity {

    Button button_stop_conversation, button_settings;
    ImageButton button_happy, button_angry, button_surprise, button_sad, button_fear, button_disgust;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_conversation);
        button_stop_conversation = findViewById(R.id.button_stop_gespreksmodus);
        button_settings = findViewById(R.id.button_Instellingen);
        button_happy = findViewById(R.id.button_toggle_happy);
        button_angry = findViewById(R.id.button_toggle_angry);
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
                startActivity(new Intent(ConversationActivity.this, ConversationSettingsActivity.class));
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

        button_surprise.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Application.cubi.ToggleEmotionBlacklisted("SURPRISE");
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
    }

    private void updateUI()
    {
        if(Application.cubi.findEmotion("HAPPY").isBlacklisted())
        {
            button_happy.setImageResource(R.drawable.ic_visibility);
        }
        else button_happy.setImageResource(R.color.green);

        if(Application.cubi.findEmotion("ANGRY").isBlacklisted()) {
            //button_angry
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
    }

}

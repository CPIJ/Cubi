package com.cubi.app.Conversation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;

import com.cubi.app.Communication.Application;
import com.cubi.app.Communication.Socket_Client;
import com.cubi.app.R;

public class ConversationSettingsActivity extends AppCompatActivity {

    private static RadioGroup radio_group;
    private static RadioButton radio_niveau1, radio_niveau2, radio_niveau3, radio_b;
    private static Button button_save;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_conversation_settings);

        button_save = findViewById(R.id.button_save);
        radio_group = findViewById(R.id.radioGroup);
        radio_niveau1 = findViewById(R.id.radioButton_niveau1);
        radio_niveau2 = findViewById(R.id.radioButton_niveau1);
        radio_niveau3 = findViewById(R.id.radioButton_niveau1);

        button_save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               int selected_id = radio_group.getCheckedRadioButtonId();
                radio_b = findViewById(selected_id);
                Application.application.control_logic("SET_LEVEL:" + radio_b.getTag());
                finish();
            }
        });
    }
}

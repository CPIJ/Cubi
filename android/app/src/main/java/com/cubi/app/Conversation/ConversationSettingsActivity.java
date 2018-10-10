package com.cubi.app.Conversation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import com.cubi.app.Communication.Application;
import com.cubi.app.Communication.Socket_Client;
import com.cubi.app.R;

public class ConversationSettingsActivity extends AppCompatActivity {

    private static RadioGroup radio_group;
    private static RadioButton radio_niveau1, radio_niveau2, radio_niveau3, radio_b;
    private static Button button_save;
    private static TextView textView_niveau;
    private int test = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_conversation_settings);

        button_save = findViewById(R.id.button_save);
        radio_group = findViewById(R.id.radioGroup);
        radio_niveau1 = findViewById(R.id.radioButton_niveau1);
        radio_niveau2 = findViewById(R.id.radioButton_niveau2);
        radio_niveau3 = findViewById(R.id.radioButton_niveau3);

        button_save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               int selected_id = radio_group.getCheckedRadioButtonId();
                radio_b = findViewById(selected_id);
                if(selected_id == radio_niveau1.getId())
                {
                    Application.cubi.control_niveau(1);
                }
                 if(selected_id == radio_niveau2.getId())
                {
                    Application.cubi.control_niveau(2);
                }
                if(selected_id == radio_niveau3.getId())
                {
                    Application.cubi.control_niveau(3);
                }
                finish();
            }
        });
        updateNiveau();

    }

    private void updateNiveau()
    {
        int niveau = Application.cubi.getNiveau();
        if(niveau == 1)
        {
            radio_niveau1.setChecked(true);
        }
        else if (niveau == 2)
        {
            radio_niveau1.setChecked(false);
            radio_niveau2.setChecked(true);
           // radio_niveau1.setChecked(false);
        }

        else if (niveau == 3)
        {
            radio_niveau3.setChecked(true);
        }
    }
}

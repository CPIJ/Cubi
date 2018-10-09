package com.cubi.app;

import com.cubi.app.Communication.Application;

import java.util.ArrayList;

public class Cubi
{
    private String state = "";
    private ArrayList<Emotion> blacklist;

    public Cubi ()
    {
        blacklist = new ArrayList<>();
    }


    public ArrayList<Emotion> getBlacklist() {
        return blacklist;
    }

    public Emotion findEmotion(String emotionName)
    {
        for (Emotion e : blacklist)
        {
            if (e.getName() == emotionName)
            {
                return e;
            }
        }
        return null;
    }


    public boolean checkInBlacklist(Emotion emotion)
    {
        for (Emotion e : blacklist)
        {
            if (e.getName() == emotion.getName())
            {
                return true;
            }
        }
        return false;
    }

    public void addEmotionToBlacklist(Emotion emotion)
    {
        if(!checkInBlacklist(emotion))
        {
            blacklist.add(emotion);
        }
    }

    public void deleteEmotionFromBlacklist(Emotion emotion)
    {
        if(!checkInBlacklist(emotion))
        {
            return;
        }
        blacklist.remove(emotion);
    }

    public void ToggleEmotionBlacklisted(String emotionName)
    {
        Emotion emotion = findEmotion(emotionName);
        if(checkInBlacklist(emotion))
        {
            deleteEmotionFromBlacklist(emotion);
        }
        else
        {
            addEmotionToBlacklist(emotion);
        }
        Application.communicator.control_logic("TOGGLE_EMOTION:" + emotionName);
    }





}

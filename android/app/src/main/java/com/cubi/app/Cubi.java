package com.cubi.app;

import com.cubi.app.Communication.Application;

import java.util.ArrayList;

public class Cubi
{
    private String state = "";
    private ArrayList<Emotion> blacklist;
    private ArrayList<Emotion> emotions;

    private void addEmotions()
    {
        emotions.add(new Emotion("HAPPY"));
        emotions.add(new Emotion("ANGRY"));
        emotions.add(new Emotion("DISGUST"));
        emotions.add(new Emotion("SURPRISE"));
        emotions.add(new Emotion("FEAR"));
        emotions.add(new Emotion("SAD"));

    }


    public Cubi ()
    {
        blacklist = new ArrayList<>();
        emotions = new ArrayList<>();
        addEmotions();
    }


    public ArrayList<Emotion> getBlacklist() {
        return blacklist;
    }

    public Emotion findEmotion(String emotionName)
    {
        for (Emotion e : emotions)
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
           if( blacklist.add(emotion)) emotion.setBlacklisted(true);
        }

    }

    public void deleteEmotionFromBlacklist(Emotion emotion)
    {
        if(!checkInBlacklist(emotion))
        {
            return;
        }
        if(blacklist.remove(emotion)) emotion.setBlacklisted(false);
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

package com.cubi.app;

import java.util.ArrayList;
import java.util.List;

public class Cubi
{
    private String state = "";
    private ArrayList<String> blacklist;

    public Cubi ()
    {
        blacklist = new ArrayList<>();
    }


    public ArrayList<String> getBlacklist() {
        return blacklist;
    }

    public boolean checkifInBlacklist(String emotion)
    {
        for (String e : blacklist)
        {
            if (e == emotion)
            {
                return true;
            }
        }
        return false;
    }

    public void addEmotionToBlacklist(String emotion)
    {
        if(!checkifInBlacklist(emotion))
        {
            blacklist.add(emotion);
        }
    }

    public void deleteEmotionFromBlacklist(String emotion)
    {
        if(!checkifInBlacklist(emotion))
        {
            return;
        }
        blacklist.remove(emotion);
    }




}

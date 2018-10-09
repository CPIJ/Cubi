package com.cubi.app;

public class Emotion
{
    private String name;
    private boolean blacklisted;

    public Emotion (String name)
    {
        this.name = name;
        this.blacklisted = false;
    }

    public String getName() {
        return name;
    }

    public boolean isBlacklisted() {
        return blacklisted;
    }

    public void setBlacklisted(boolean bool) {
        blacklisted = bool;
    }
}

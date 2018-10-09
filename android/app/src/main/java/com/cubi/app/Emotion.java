package com.cubi.app;

public class Emotion
{
    private static String name;
    private static boolean blacklisted;

    public Emotion (String name,  boolean blacklisted)
    {
        this.name = name;
        this.blacklisted = blacklisted;
    }

    public static String getName() {
        return name;
    }

    public static boolean isBlacklisted() {
        return blacklisted;
    }

    public static void setBlacklisted(boolean blacklisted) {
        Emotion.blacklisted = blacklisted;
    }
}

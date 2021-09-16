package gatech;

import java.io.Serializable;

public class Event implements Serializable{
    private String eventType;
    private String eventFullName;
    private String eventMakerName;
    private Studio eventMaker;
    private int eventYear;
    private int eventDuration;
    private int eventLicenseFee;



    public Event(String eventType, String eventFullName, Integer eventYear, Integer eventDuration,
                 Studio eventMaker, Integer eventLicenseFee) {
        this.eventFullName = eventFullName;
        this.eventType = eventType;
        this.eventYear = eventYear;
        this.eventDuration = eventDuration;
        this.eventMaker = eventMaker;
        this.eventMakerName = eventMaker.get_shortname();
        this.eventLicenseFee = eventLicenseFee;
    }

    public String[] display_event() {
        System.out.println(eventType + "," + eventFullName + "," + eventYear + "," + eventDuration + "," + eventMakerName + "," + eventLicenseFee);
        String[] result ={eventType, eventFullName, String.valueOf(eventYear),
                            String.valueOf(eventDuration), eventMakerName, String.valueOf(eventLicenseFee)};
        return result;
    }

    public String get_event_type() {
        return eventType;
    }
    public String get_event_fullname(){
        return eventFullName;
    }
    public int get_event_year(){
        return eventYear;
    }
    public int get_event_licensefee(){
        return eventLicenseFee;
    }
    public String get_event_makername(){
        return eventMakerName;
    }

}

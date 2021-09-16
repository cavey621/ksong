package gatech;

import java.util.HashMap;
import java.util.Map;
import java.io.Serializable;
import java.util.LinkedHashMap;

public class Streaming implements Serializable{
    private String streamShortName;
    private String streamLongName;
    private int streamSubscription;
    private int streamCurrentRevenue;
    private int streamPreviousRevenue;
    private int streamTotalRevenue;
    private int streamLicensing;
    private LinkedHashMap<String, Integer> streamRevenueHistory;

    // < (eventname + eventyear), subscription >
    Map<String, Integer> eventOfferedList;

    public Streaming(String streamShortName, String streamLongName, int streamSubscription){
        this.streamShortName = streamShortName;
        this.streamLongName = streamLongName;
        this.streamSubscription = streamSubscription;
        this.streamCurrentRevenue = 0;
        this.streamPreviousRevenue = 0;
        this.streamTotalRevenue = 0;
        this.streamLicensing = 0;
        this.eventOfferedList = new HashMap<>();
        this.streamRevenueHistory = new LinkedHashMap<String, Integer>();

    }

    public void add_offered_event(Event event, int offerPrice) {
        String event_name = event.get_event_fullname() + event.get_event_year();
        // when a event is offered, then it is included
        if ( event.get_event_type().equals("ppv") ){
            eventOfferedList.put(event_name, offerPrice);
        } else if ( event.get_event_type().equals("movie") ){
            eventOfferedList.put(event_name, 0);
        }
    }

    // need deal with money inflow and outflow
    public void get_subscription_paid(int new_payment){
        streamCurrentRevenue += new_payment;
    }

    public void pay_license(Event event){
        streamLicensing += event.get_event_licensefee();
    }

    public String get_shortname(){
        return streamShortName;
    }

    public int get_subscription(){
        return streamSubscription;
    }

    public int get_offeredevent_ppvfee(String event_name ){
        return eventOfferedList.get(event_name);
    }

    public void next_month(){
        streamTotalRevenue += streamCurrentRevenue;
        streamPreviousRevenue = streamCurrentRevenue;
        String currDate = TestCaseReader.getMonthTimeStamp() + "/" + TestCaseReader.getYearTimeStamp();
        streamRevenueHistory.put(currDate, streamCurrentRevenue);
        streamCurrentRevenue = 0;
        eventOfferedList.clear();
    }

    public Object[][] display_streaming(){
        System.out.println("stream," + streamShortName + "," + streamLongName);
        System.out.println("subscription," + streamSubscription);
        System.out.println("current_period," + streamCurrentRevenue);
        System.out.println("previous_period," + streamPreviousRevenue);
        System.out.println("total," + streamTotalRevenue);
        System.out.println("licensing," + streamLicensing);
        Object[][] result = {{"stream,", streamShortName + "," + streamLongName},{"subscription,", streamSubscription},
                {"current_period," , streamCurrentRevenue},{"previous_period," , streamPreviousRevenue},
                {"total," ,streamTotalRevenue},{"licensing,",streamLicensing}};
        return result;
    }

    public LinkedHashMap<String, Integer> getStreamRevenueHistory() {
        return streamRevenueHistory;
    }
}

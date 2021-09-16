package gatech;

import java.lang.*;
import java.util.HashMap;
import java.util.Map;
import java.io.Serializable;
import java.util.LinkedHashMap;


public class Demographic implements Serializable{
    private String demoShortName;
    private String demoLongName;
    private int demoAccounts;
    private int demoCurrentSpending;
    private int demoPreviousSpending;
    private int demoTotalSpending;
    private LinkedHashMap<String, Integer> demoSpendingHistory;


    // movie subscription
    Map<String, Integer> subscriptionList;
    // only for ppv event due to re-watching policy complication
    Map<String, Integer> demoWatchingHistory;

    public Demographic (String demoShortName, String demoLongName, int demoAccounts) {
        this.demoShortName = demoShortName;
        this.demoLongName = demoLongName;
        this.demoAccounts = demoAccounts;
        this.demoCurrentSpending = 0;
        this.demoPreviousSpending = 0;
        this.demoTotalSpending = 0;
        this.demoSpendingHistory = new LinkedHashMap<String, Integer>();


        this.subscriptionList = new HashMap<>();
        this.demoWatchingHistory = new HashMap<>();
    }

    // Need to find PPV_fee from offered event and feed into this program
    public int watch_event(Event event, Streaming streaming, int percentage){
        int new_watch_event_account = (int) Math.ceil(percentage / 100.0 * demoAccounts);
        int new_payment = 0;

        // differentiate eventType
        if (event.get_event_type().equals("movie")){
            String streaming_shortname = streaming.get_shortname();
            if (subscriptionList.containsKey(streaming_shortname)){
                int current_watch_event_account = subscriptionList.get(streaming_shortname);
                if (new_watch_event_account > current_watch_event_account) {
                    new_payment = (new_watch_event_account - current_watch_event_account) * streaming.get_subscription();
                    // update new and larger account number for this streaming service
                    subscriptionList.replace(streaming_shortname, new_watch_event_account);
                }
            } else {
                // it is a new streaming service
                new_payment = new_watch_event_account * streaming.get_subscription();
                // insert the viewer number for this streaming service
                subscriptionList.put(streaming_shortname, new_watch_event_account);
            }
        } else if (event.get_event_type().equals("ppv")) {
            String event_name = event.get_event_fullname() + event.get_event_year();
            int PPV_fee = streaming.get_offeredevent_ppvfee(event_name);
            if (demoWatchingHistory.containsKey(event_name)){
                // Re-watching is always free
                int current_watch_event_account = demoWatchingHistory.get(event_name);
                if (new_watch_event_account > current_watch_event_account) {
                    new_payment = (new_watch_event_account - current_watch_event_account) * PPV_fee;
                    // update new and larger account number for this streaming service
                    demoWatchingHistory.replace(event_name, new_watch_event_account);
                }
            } else {
                // it is a new event
                new_payment = new_watch_event_account * PPV_fee;
                // insert event into
                demoWatchingHistory.put(event_name, new_watch_event_account);
            }
        }

        // update new payment
        demoCurrentSpending += new_payment;

        return new_payment;
    }


    public Object[][] display_demo() {
//        System.out.println("Enter display_demo in Demographic.java");
//        System.out.println("demo," + demoShortName + "," + demoLongName);
//        System.out.println("size," + demoAccounts);
//        System.out.println("current_period," + demoCurrentSpending);
//        System.out.println("previous_period," + demoPreviousSpending);
//        System.out.println("total," + demoTotalSpending);
        Object[][] result = {{"demo", demoShortName + "," + demoLongName}, {"size", demoAccounts},
                {"current_period", demoCurrentSpending}, {"previous_period", demoPreviousSpending},
                {"total" , demoTotalSpending}};
        return result;
    }

    public void next_month(){
        demoTotalSpending += demoCurrentSpending;
        demoPreviousSpending = demoCurrentSpending;

        String currDate = TestCaseReader.getMonthTimeStamp() + "/" + TestCaseReader.getYearTimeStamp();
        demoSpendingHistory.put(currDate, demoCurrentSpending);

        demoCurrentSpending = 0;

        // clean stored history
        subscriptionList.clear();
        demoWatchingHistory.clear();
    }

    public LinkedHashMap<String, Integer> getDemoSpendingHistory() {
        return demoSpendingHistory;
    }

}

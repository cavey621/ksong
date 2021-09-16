package gatech;

import java.io.*;
import java.util.*;

public class TestCaseReader {
    // create an eventList
    private List<Event> eventList;
    Map<String, Event> eventMap;
    private List<Transaction> offerList;
    Map<String, Transaction> offerMap;

    Map<String, Demographic> demoList;
    Map<String, Streaming> streamList;
    Map<String, Studio> studioList;

    private static int monthTimeStamp;
    private static int yearTimeStamp;

    private Object[][] stringoutput;
    private Object[][] eventDisplayOutput;


    public TestCaseReader() {
        eventList  = new ArrayList<>();
        eventMap   = new HashMap<>();
        offerList  = new ArrayList<>();
        offerMap   = new HashMap<>();

        demoList   = new HashMap<>();
        streamList = new HashMap<>();
        studioList = new HashMap<>();

        monthTimeStamp = 10;
        yearTimeStamp = 2020;

    }
    public Boolean check_file_existed(String filename){
        File f = new File(filename);
        if(f.exists() && !f.isDirectory()) {
            return(Boolean.TRUE);
        }else{
            return(Boolean.FALSE);
        }
    }

    public void start_new_data(){
        eventList  = new ArrayList<>();
        eventMap   = new HashMap<>();
        offerList  = new ArrayList<>();
        offerMap   = new HashMap<>();

        demoList   = new HashMap<>();
        streamList = new HashMap<>();
        studioList = new HashMap<>();

        stringoutput = new Object[][] {{"",""},{"",""}};
        eventDisplayOutput = new Object[][] {{"",""},{"",""}};

        monthTimeStamp = 10;
        yearTimeStamp = 2020;
    }

    public void save_data() throws IOException {
        System.out.println("saving in eventList");
        WriterReader.write_event_list("eventList.txt", this.eventList);
        System.out.println("saving in offerList");
        WriterReader.write_transaction_list("offerList.txt", this.offerList);
        WriterReader.write_event_map("eventMap.txt", this.eventMap);
        WriterReader.write_transaction_map("offerMap.txt", this.offerMap);
        WriterReader.write_demo_map("demoList.txt", this.demoList);
        WriterReader.write_stream_map("streamList.txt", this.streamList);
        System.out.println("saving in studioList");
        WriterReader.write_studio_map("studioList.txt", this.studioList);

        int[] timeStamp;
        timeStamp = new int[]{this.yearTimeStamp, this.monthTimeStamp};
        WriterReader.write_timeStamp_list("timeStamp.txt", timeStamp);
    }

    public void read_data() throws IOException, ClassNotFoundException {

        if (check_file_existed("eventList.txt")){
            System.out.println("reading in eventList");
            this.eventList = WriterReader.read_event_list("eventList.txt");
        }

        if (check_file_existed("offerList.txt")){
            System.out.println("reading in offerList");
            this.offerList = WriterReader.read_transaction_list("offerList.txt");
        }

        if (check_file_existed("eventMap.txt")){
            System.out.println("reading in eventMap");
            this.eventMap = WriterReader.read_event_map("eventMap.txt");
        }

        if (check_file_existed("offerMap.txt")){
            this.offerMap = WriterReader.read_transaction_map("offerMap.txt");
        }

        if (check_file_existed("demoList.txt")){
            this.demoList = WriterReader.read_demo_map("demoList.txt");
        }

        if (check_file_existed("streamList.txt")){
            this.streamList = WriterReader.read_stream_map("streamList.txt");
        }

        if (check_file_existed("studioList.txt")){
            System.out.println("reading in studioList");
            this.studioList = WriterReader.read_studio_map("studioList.txt");
        }

        if (check_file_existed("timeStamp.txt")){
            int[] timeStamp = WriterReader.read_timeStamp_list("timeStamp.txt");
            this.yearTimeStamp = timeStamp[0];
            this.monthTimeStamp = timeStamp[1];
        }
    }

    public Object[][] getStringoutput() {
        return this.stringoutput;
    }

    public Object[][] getEventDisplayOutput() {
        return this.eventDisplayOutput;
    }

    /* If saved files exist, read it first by REQUSET*/
//        read_data();
    public int processInstructions(String[] tokens) throws IOException, ClassNotFoundException {
        /* pre-declaration */
        String event_name;

        switch (tokens[0]) {
            case "create_demo": {
                Demographic new_demo = new Demographic(tokens[1], tokens[2], Integer.parseInt(tokens[3]));
                //register
                demoList.put(tokens[1], new_demo);
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;
            }
            case "create_studio":
                Studio new_studio = new Studio(tokens[1], tokens[2]);
                //register
                studioList.put(tokens[1], new_studio);
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;
            case "create_event":
                // need to know if eventMaker(Studio) exists
                if (!studioList.containsKey(tokens[5])) {
                    return -1;
                }

                Event new_event = new Event(tokens[1], tokens[2], Integer.parseInt(tokens[3]), Integer.parseInt(tokens[4]),
                        studioList.get(tokens[5]), Integer.parseInt(tokens[6]));
                // register the new event
                eventList.add(new_event);
                event_name = tokens[2] + tokens[3];
                eventMap.put(event_name, new_event);
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;
            case "create_stream": {
                Streaming new_streaming = new Streaming(tokens[1], tokens[2], Integer.parseInt(tokens[3]));
                //register
                streamList.put(tokens[1], new_streaming);
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;
            }
            case "offer_movie":
            case "offer_ppv": {
                event_name = tokens[2] + tokens[3];
                // pre-check: 1)the existence of event (assuming studio is already checked in creat_event ); 2) streaming
                if ( !(eventMap.containsKey(event_name) && streamList.containsKey(tokens[1])) )  {
                    return -1;
                }

                String offerType = tokens[0].substring(6);
                Event event_offer = eventMap.get(event_name);
                Studio studio_offer = studioList.get(event_offer.get_event_makername());
                Streaming streaming_offer = streamList.get(tokens[1]);

                int offerPrice = 0;
                if (offerType.equals("ppv")) {
                    offerPrice = Integer.parseInt(tokens[4]);
                }

                Transaction new_transaction = new Transaction(event_offer, streaming_offer, studio_offer, offerPrice);
                // process the offer transaction
                new_transaction.process_licensing();
                // register offer list and map
                offerList.add(new_transaction);
                offerMap.put(event_name, new_transaction);
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;
            }
            case "watch_event": {
                String watchDemoGroup = tokens[1];
                int watchPercentage = Integer.parseInt(tokens[2]);
                String watchStream = tokens[3];
                String watchEventName = tokens[4];
                int watchEventYear = Integer.parseInt(tokens[5]);
                event_name = watchEventName + watchEventYear;

                // pre-check: 1) demo is created; 2) this event is offered (assuming in OfferEvent, we already check
                // the existence of event, streaming, and studio);
                if ( !(demoList.containsKey(watchDemoGroup) && offerMap.containsKey(event_name)) ) {
                    return -1;
                }

                // find inputs
                Demographic new_demo = demoList.get(watchDemoGroup);
                new_event = eventMap.get(event_name);
                Streaming new_streaming = streamList.get(watchStream);

                // demo needs to calculate the subscription payment to streaming and updates its spending account
                int subscription_payment_demo = new_demo.watch_event(new_event, new_streaming, watchPercentage);

                // streaming will get paid and update its revenue
                System.out.println("Before Watching event, streaming get subscription  = " + new_streaming.get_subscription());
                new_streaming.get_subscription_paid(subscription_payment_demo);
                System.out.println("After Watching event, streaming get subscription paid = " + new_streaming.get_subscription());
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;
            }
            case "next_month":


                // Update current, previous and total dollar amounts
                // demographic
                for (Demographic demo : demoList.values()) {
                    demo.next_month();
                }
                // streaming
                for (Streaming streaming : streamList.values()) {
                    streaming.next_month();
                }
                // studio
                for (Studio studio : studioList.values()) {
                    studio.next_month();
                }

                // Update the current timestamp
                if (monthTimeStamp == 12) {
                    yearTimeStamp++;
                }
                monthTimeStamp = (monthTimeStamp % 12) + 1;

                // empty offerList and offerMap
                offerList = new ArrayList<>();
                offerMap.clear();
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;
            case "display_demo": {
//                System.out.println("Enter Display demo in test case reader");
//                System.out.println("Print tokens:" + tokens[1]);
                if (demoList.containsKey(tokens[1])){
//                    System.out.println("Prepare to read data");
                    this.stringoutput = demoList.get(tokens[1]).display_demo();
//                    System.out.println("--------get Data--------");
//                    System.out.println(stringoutput[0][0].toString());
                }
                break;
            }
            case "display_events":
                System.out.println("Enter display_events in TestCaseReader.java");
                System.out.println("evetnList size = " + eventList.size());

                String[][] tank = new String[eventList.size() + 1][6];
                tank[0] = new String[] {"Type", "Name", "Year Produced", "Duration", "Studio","License Fee"};
                for (int i=1; i < eventList.size() + 1; i++) {
                    tank[i] = eventList.get(i - 1).display_event();
                }
                eventDisplayOutput = tank;
                break;
            case "display_stream":
                if (streamList.containsKey(tokens[1])){
                    this.stringoutput = streamList.get(tokens[1]).display_streaming();
                }

                break;
            case "display_studio":
                if (studioList.containsKey(tokens[1])){
                    this.stringoutput = studioList.get(tokens[1]).display_studio();
                }

                break;
            case "display_offers":
                System.out.println("Enter display_offers in TestCaseReader.java");

                String[][] tank2 = new String[offerList.size()+1][5];
                tank2[0] = new String[]{"Stream", "Type", "Short Name", "Year", "Subscription price (only) if ppv"};
                for (int i=1; i<(offerList.size()+1); i++) {
                    tank2[i] = offerList.get(i-1).display_offers();
                }
                eventDisplayOutput = tank2;

                break;
            case "display_time":
                System.out.println("time," + monthTimeStamp + "," + yearTimeStamp);
                break;
            case "display_demo_spending_history":
                if (demoList.containsKey(tokens[1])) {
                    System.out.println(demoList.get(tokens[1]).getDemoSpendingHistory());

                    this.stringoutput = linkedHashMap_to_2Darr(
                        demoList.get(tokens[1]).getDemoSpendingHistory());
                }else {
                    this.stringoutput = new Object[][]{{"Date","Dollar Amount($)"}};

                }
                break;
            case "display_stream_revenue_history":
                if (streamList.containsKey(tokens[1])) {
                    System.out.println(streamList.get(tokens[1]).getStreamRevenueHistory());
                    stringoutput = linkedHashMap_to_2Darr(streamList.get(tokens[1]).getStreamRevenueHistory());

                } else {
                    this.stringoutput = new Object[][]{{"Date","Dollar Amount($)"}};
                }

                break;
            case "display_studio_revenue_history":
                if (studioList.containsKey(tokens[1])) {
                    System.out.println(studioList.get(tokens[1]).getStudioRevenueHistory());
                    this.stringoutput = linkedHashMap_to_2Darr(studioList.get(tokens[1]).getStudioRevenueHistory());

                } else {
                    this.stringoutput = new Object[][]{{"Date","Dollar Amount($)"}};

                }
                break;

            case "set_month":
                monthTimeStamp = Integer.parseInt(tokens[1]);
                yearTimeStamp = Integer.parseInt(tokens[2]);
                /* Save to the local drive, the decision to save or not is by REQUEST*/
                save_data();
                break;

        }

//        /* Save to the local drive, the decision to save or not is by REQUEST*/
//        save_data();

        /* If all goes successfully, then return 0*/
        return 0;
    }

    public Object[][] linkedHashMap_to_2Darr(LinkedHashMap<String, Integer> hm){

        String[][] arr = new String[hm.size()+1][2];
        arr[0] = new String[] {"Date", "Dollar Amount($)"};

        if (!hm.isEmpty()) {
            int i = 1;
            for (Map.Entry mapElement : hm.entrySet()) {
                String key = (String) mapElement.getKey();
                String value = String.valueOf(mapElement.getValue());
                arr[i++] = new String[] {key, value};
            }
        }
        return arr;
    }

    public static int getMonthTimeStamp() {
        return monthTimeStamp;
    }

    public static int getYearTimeStamp() {
        return yearTimeStamp;
    }

    public static void setMonthTimeStamp(int monthTimeStamp) {
        TestCaseReader.monthTimeStamp = monthTimeStamp;
    }

    public static void setYearTimeStamp(int yearTimeStamp) {
        TestCaseReader.yearTimeStamp = yearTimeStamp;
    }
}

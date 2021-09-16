package gatech;

import java.io.Serializable;

public class Transaction implements Serializable {
    private String offerType;
//    private String offerEventFullName;
    private int offerYear;
    private int offerPPVFee;
    private Event offerEvent;
    private Streaming offerStreaming;
    private Studio offerStudio;

    public Transaction(Event event, Streaming streaming, Studio studio, int offerPrice) {
        this.offerType = event.get_event_type();
//        this.offerEventFullName = event.get_event_fullname();
        this.offerYear = event.get_event_year();
        this.offerPPVFee = offerPrice;

        this.offerEvent = event;
        this.offerStreaming = streaming;
        this.offerStudio = studio;
    }

    public void process_licensing(){
        // streaming pays for the licensing and add this event into eventOfferedList
        offerStreaming.pay_license(offerEvent);
        offerStreaming.add_offered_event(offerEvent, offerPPVFee);

        // studio takes the licensing
        offerStudio.get_licensing_paid(offerEvent);
    }

    public String[] display_offers(){
        if (offerType.equals("ppv")){
            System.out.println(offerStreaming.get_shortname()+ "," + offerType + "," + offerEvent.get_event_fullname() + "," + offerYear + "," + offerPPVFee);
            String[] result = {offerStreaming.get_shortname(), offerType, offerEvent.get_event_fullname(),
                    String.valueOf(offerYear), String.valueOf(offerPPVFee)};
            return result;
        }else{
            String[] result = {offerStreaming.get_shortname(), offerType, offerEvent.get_event_fullname(),
                    String.valueOf(offerYear), "NA"};
            return result;
        }
    }

}

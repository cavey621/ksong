package gatech;

import java.io.*;
import java.util.*;


public class WriterReader {
    // ------------------------------------------------------------------------------------------- List
    /*  ****** String list - TimeStamp ****** */
    static void write_timeStamp_list(String fileName, int[] timeStamp) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(timeStamp);

        oos.flush();
        oos.close();
    }

    static int[] read_timeStamp_list(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        int[] timeStamp = (int[]) ois.readObject();
        ois.close();
        return timeStamp;
    }


    /*  ****** Event list ****** */
    static void write_event_list(String fileName, List<Event> eventList) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(eventList);

        oos.flush();
        oos.close();
    }

    static ArrayList<Event> read_event_list(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        ArrayList<Event> eventList = (ArrayList<Event>) ois.readObject();
        ois.close();
        return eventList;
    }

    /*  ****** Transaction list ****** */
    static void write_transaction_list(String fileName, List<Transaction> offerList) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(offerList);

        oos.flush();
        oos.close();
    }

    static ArrayList<Transaction> read_transaction_list(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        ArrayList<Transaction> offerList = (ArrayList<Transaction>) ois.readObject();
        ois.close();
        return offerList;
    }

    // ------------------------------------------------------------------------------------------- HashMap
    /*  ****** Event Map ****** */
    static void write_event_map(String fileName, Map<String, Event> eventMap) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(eventMap);

        oos.flush();
        oos.close();
    }

    static Map<String, Event> read_event_map(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        Map<String, Event> eventMap = (Map<String, Event>) ois.readObject();
        ois.close();
        return eventMap;
    }

    /*  ****** Transaction Map ****** */
    static void write_transaction_map(String fileName, Map<String, Transaction> offerMap) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(offerMap);

        oos.flush();
        oos.close();
    }

    static Map<String, Transaction> read_transaction_map(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        Map<String, Transaction> offerMap = (Map<String, Transaction>) ois.readObject();
        ois.close();
        return offerMap;
    }

    /*  ****** Demo Map ****** */
    static void write_demo_map(String fileName, Map<String, Demographic> demoList) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(demoList);

        oos.flush();
        oos.close();
    }

    static Map<String, Demographic> read_demo_map(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        Map<String, Demographic> demoList = (Map<String, Demographic>) ois.readObject();
        ois.close();
        return demoList;
    }

    /*  ****** Studio Map ****** */
    static void write_studio_map(String fileName, Map<String, Studio> studioList) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(studioList);

        oos.flush();
        oos.close();
    }

    static Map<String, Studio> read_studio_map(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        Map<String, Studio> studioList = (Map<String, Studio>) ois.readObject();
        ois.close();
        return studioList;
    }

    /*  ****** Streaming Map ****** */
    static void write_stream_map(String fileName, Map<String, Streaming> streamList) throws IOException {
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(streamList);

        oos.flush();
        oos.close();
    }

    static Map<String, Streaming> read_stream_map(String fileName) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);

        Map<String, Streaming> streamList = (Map<String, Streaming>) ois.readObject();
        ois.close();
        return streamList;
    }

    // ------------------------------------------------------------------------------------------- Object
    // not necessary
    // ------------------------------------------------------------------------------------------- Date
    // private int monthTimeStamp;
    // private int yearTimeStamp;
    // Do it later;
}
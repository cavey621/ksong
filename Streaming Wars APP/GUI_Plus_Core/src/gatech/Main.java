package gatech;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // write your code here
//        DataSaver d = new DataSaver();
//        d.data();
        JFrame frame = new JFrame("Streaming Wars App");
        frame.setContentPane(new MainGUI().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setSize(500, 200);
        frame.setVisible(true);
    }
}

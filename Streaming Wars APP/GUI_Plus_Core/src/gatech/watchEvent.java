package gatech;

import javax.swing.*;

public class watchEvent {
    private JTextField demo_group;
    private JTextField stream;
    private JTextField event;
    private JTextField year;
    private JPanel watchEventPanel;
    private JButton saveButton;
    private JButton cancelButton;
    private JTextField percentage;

    public JPanel getWatchEventPanel() {
        return watchEventPanel;
    }

    public JTextField getYear() {
        return year;
    }

    public JButton getSaveButton() {
        return saveButton;
    }

    public JButton getCancelButton() {
        return cancelButton;
    }

    public JTextField getPercentage() {
        return percentage;
    }

    public JTextField getEvent() {
        return event;
    }

    public JTextField getStream() {
        return stream;
    }

    public JTextField getDemo_group() {
        return demo_group;
    }
    public void setEmpty(String s){
        this.stream.setText(s);
        this.year.setText(s);
        this.event.setText(s);
        this.percentage.setText(s);
        this.demo_group.setText(s);
    }
}

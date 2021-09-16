package gatech;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class createEvent {
    private JPanel panel1;
    private JTextField type;
    private JTextField name;
    private JTextField year_produced;
    private JTextField duration;
    private JTextField studio;
    private JTextField licence_fee;
    private JButton savebutton;
    private JButton cancelbutton;

    public JPanel getPanel1() {
        return panel1;
    }
    public JTextField getType() {
        return type;
    }
    public JTextField getName() {
        return name;
    }

    public JTextField getYear_produced() {
        return year_produced;
    }

    public JTextField getDuration() {
        return duration;
    }

    public JTextField getStudio() {
        return studio;
    }

    public JTextField getLicence_fee() {
        return licence_fee;
    }

    public JButton getCancelbutton() {
        return cancelbutton;
    }

    public JButton getSavebutton() {
        return savebutton;
    }

    public void setEmpty(String s) {
        this.type.setText(s);
        this.name.setText(s);
        this.year_produced.setText(s);
        this.duration.setText(s);
        this.studio.setText(s);
        this.licence_fee.setText(s);
    }
}

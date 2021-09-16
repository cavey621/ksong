package gatech;

import javax.swing.*;

public class createStudio {
    private JButton savebutton;
    private JTextField short_name;
    private JTextField long_name;
    private JButton cancelButton;
    private JLabel title;
    private JLabel sn;
    private JLabel ln;
    private JPanel studioPanel;

    public JPanel getStudioPanel(){
        return studioPanel;
    }

    public JButton getSavebutton() {
        return savebutton;
    }

    public JButton getCancelButton() {
        return cancelButton;
    }

    public JTextField getShort_name() {
        return short_name;
    }

    public JTextField getLong_name() {
        return long_name;
    }

    public void setShort_name(String short_name) {
        this.short_name.setText(short_name);
    }

    public void setLong_name(String long_name) {
        this.long_name.setText(long_name);
    }
}

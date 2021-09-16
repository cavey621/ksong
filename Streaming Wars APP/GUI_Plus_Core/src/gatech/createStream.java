package gatech;

import javax.swing.*;

public class createStream {
    private JTextField short_name;
    private JTextField long_name;
    private JTextField sub_price;
    private JButton saveButton;
    private JButton cancelButton;
    private JPanel streamPanel;

    public JPanel getStreamPanel() {
        return streamPanel;
    }

    public JTextField getShort_name() {
        return short_name;
    }

    public JTextField getLong_name() {
        return long_name;
    }

    public JTextField getSub_price() {
        return sub_price;
    }

    public JButton getSaveButton() {
        return saveButton;
    }

    public JButton getCancelButton() {
        return cancelButton;
    }

    public void setEmpty(String s){
        this.short_name.setText(s);
        this.long_name.setText(s);
        this.sub_price.setText(s);
    }
}

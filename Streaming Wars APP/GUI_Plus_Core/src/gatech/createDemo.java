package gatech;

import javax.swing.*;

public class createDemo {
    private JPanel enterDataPanel;
    private JLabel title;
    public JTextField number_of_accounts;
    public JTextField long_name;
    public JTextField short_name;
    private JLabel ln;
    private JLabel number;
    private JLabel sn;
    private JButton savebutton;
    private JButton cancelButton;
    private JFrame f = new JFrame("Enter Data");

    public JPanel getEnterDataPanel(){
        return enterDataPanel;
    }

    public JButton getSavebutton(){
        return savebutton;
    }

    public JButton getCancelButton(){
        return cancelButton;
    }

    public void setLong_name(String long_name) {
        this.long_name.setText(long_name);
    }

    public void setShort_name(String short_name){
        this.short_name.setText(short_name);
    }

    public void setNumber_of_accounts(String number_of_accounts){
        this.number_of_accounts.setText(number_of_accounts);
    }
}

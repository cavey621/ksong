package gatech;

import javax.swing.*;

public class offerPPV {
    private JTextField stream;
    private JTextField ppv_name;
    private JTextField year;
    private JTextField view_price;
    private JButton saveButton;
    private JButton cancelButton;
    private JPanel offerPPVPanel;

    public JTextField getStream() {
        return stream;
    }

    public JTextField getPpv_name() {
        return ppv_name;
    }

    public JTextField getYear() {
        return year;
    }

    public JTextField getView_price() {
        return view_price;
    }

    public JButton getSaveButton() {
        return saveButton;
    }

    public JButton getCancelButton() {
        return cancelButton;
    }

    public JPanel getOfferPPVPanel() {
        return offerPPVPanel;
    }

    public void setEmpty(String s){
        this.ppv_name.setText(s);
        this.year.setText(s);
        this.stream.setText(s);
        this.view_price.setText(s);
    }
}

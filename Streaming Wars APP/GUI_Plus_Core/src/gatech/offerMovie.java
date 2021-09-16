package gatech;

import javax.swing.*;

public class offerMovie {
    private JTextField stream;
    private JTextField movie;
    private JTextField year;
    private JButton saveButton;
    private JButton cancelButton;
    private JPanel offerMovie;

    public JTextField getStream() {
        return stream;
    }

    public JTextField getMovie() {
        return movie;
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

    public JPanel getOfferMovie() {
        return offerMovie;
    }

    public void setEmpty(String s) {
        this.stream.setText(s);
        this.movie.setText(s);
        this.year.setText(s);
    }

}

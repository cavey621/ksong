package gatech;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.*;

public class MainGUI {
    private String[] tokens;

    private JLabel currentDate;
    public JPanel mainPanel;
    private JComboBox commandList;
    private JButton newData;
    private JButton retrieveData;
    private JButton nextMonthButton;
    private JButton setMonthButton;
    private JTextField monthTextField;
    private JTextField yearTextField;
    private JButton showFinancialDataButton;

    private String sel;

    public JFrame ndframe = new JFrame("Enter Data");
    private createDemo demo = new createDemo();
    private createStudio studio = new createStudio();
    private createEvent event = new createEvent();
    private createStream stream = new createStream();
    private offerMovie offm = new offerMovie();
    private offerPPV offppv = new offerPPV();
    private watchEvent watche = new watchEvent();
    private displayData displayd = new displayData();
    private displayEvents displaye = new displayEvents();
    private displayOffers displayo = new displayOffers();
    private displayFinancial displayf = new displayFinancial();

    private TestCaseReader caseScanner = new TestCaseReader();

    public MainGUI() {
        currentDate.setText("Current Time: "+TestCaseReader.getMonthTimeStamp()+" ," + TestCaseReader.getYearTimeStamp());
        setMonthButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                caseScanner.start_new_data();
                int month = Integer.parseInt(monthTextField.getText());
                int year = Integer.parseInt(yearTextField.getText());
                TestCaseReader.setMonthTimeStamp(month);
                TestCaseReader.setYearTimeStamp(year);
                monthTextField.setText("month");
                yearTextField.setText("year");
                currentDate.setText("Current Time: "+month+" ,"+year);

                setMonthButton.setEnabled(false);
            }
        });
        /* click newData Button to clean out everything */
        newData.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                TestCaseReader.setMonthTimeStamp(10);
                TestCaseReader.setYearTimeStamp(2020);
                currentDate.setText("Current Time: "+TestCaseReader.getMonthTimeStamp()+" ," + TestCaseReader.getYearTimeStamp());
                monthTextField.setText("month");
                yearTextField.setText("year");
                caseScanner.start_new_data();
                setMonthButton.setEnabled(true);
            }
        } );

        /* click Retrieve Button to read the old data*/
        retrieveData.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    System.out.println("retrieveData starts in MainGUI");
                    caseScanner.read_data();
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
            }
        } );

        /* initiation */
        commandList.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JComboBox cb = (JComboBox)e.getSource();
                String command = (String)cb.getSelectedItem();
                switch (command){
                    case "Create Demo":
                        ndframe.setContentPane(demo.getEnterDataPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        break;
                    case "Create Studio":
                        ndframe.setContentPane(studio.getStudioPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        break;
                    case "Create Event":
                        ndframe.setContentPane(event.getPanel1());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        break;
                    case "Create Stream":
                        ndframe.setContentPane(stream.getStreamPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        break;
                    case "Offer Movie":
                        ndframe.setContentPane(offm.getOfferMovie());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        break;
                    case "Offer PPV":
                        ndframe.setContentPane(offppv.getOfferPPVPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        break;
                    case "Watch Event":
                        ndframe.setContentPane(watche.getWatchEventPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        break;
                    case "Display Data":
                        ndframe.setContentPane(displayd.getDisplayPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        ndframe.setSize(500, 400);
                        break;
                    case "Display Events":

                        ndframe.setContentPane(displaye.getDisplayEventPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        ndframe.setSize(600, 500);
                        try {
                            caseScanner.processInstructions(new String[]{"display_events"});
                            displaye.settableData(caseScanner.getEventDisplayOutput());
                        } catch (IOException ioException) {
                            ioException.printStackTrace();
                        } catch (ClassNotFoundException classNotFoundException) {
                            classNotFoundException.printStackTrace();
                        }
                        break;
                    case "Display Offers":
                        ndframe.setContentPane(displayo.getDisplayOfferPanel());
                        ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                        ndframe.pack();
                        ndframe.setSize(600, 500);

                        try {
                            caseScanner.processInstructions(new String[]{"display_offers"});
                            displayo.settableData(caseScanner.getEventDisplayOutput());
                        } catch (IOException ioException) {
                            ioException.printStackTrace();
                        } catch (ClassNotFoundException classNotFoundException) {
                            classNotFoundException.printStackTrace();
                        }
                        break;
                }
                ndframe.setVisible(true);
            }
        });

        demo.getSavebutton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String short_name = demo.short_name.getText();
                String long_name = demo.long_name.getText();
                String number = demo.number_of_accounts.getText();
                System.out.println(short_name + ", " +long_name+", "+ number);
                /* Execute the testreader*/
                String[] tokens = {"create_demo",short_name, long_name, number};
                try {
                    caseScanner.processInstructions(tokens);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                demo.setLong_name("");
                demo.setNumber_of_accounts("");
                demo.setShort_name("");
                ndframe.dispose();
            }
        });

        demo.getCancelButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.dispose();
            }
        });

        studio.getSavebutton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String short_name = studio.getShort_name().getText();
                String long_name = studio.getLong_name().getText();
                System.out.println(short_name + ", " +long_name);
                /* Execute the testreader*/
                String[] tokens = {"create_studio",short_name, long_name};
                try {
                    caseScanner.processInstructions(tokens);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                studio.setLong_name("");
                studio.setShort_name("");
                ndframe.dispose();
            }
        });
        studio.getCancelButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.dispose();
            }
        });

        event.getSavebutton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String type = event.getType().getText();
                String name = event.getName().getText();
                String year = event.getYear_produced().getText();
                String duration = event.getDuration().getText();
                String stu = event.getStudio().getText();
                String licence_fee = event.getLicence_fee().getText();
                System.out.println(type + ", " +name + " ," + year + " ,"+duration + " ," + stu + " ," + licence_fee);
                /* Execute the testreader*/
                String[] tokens = {"create_event", type, name, year, duration, stu, licence_fee};
                try {
                    caseScanner.processInstructions(tokens);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                event.setEmpty("");
                ndframe.dispose();
            }
        });
        event.getCancelbutton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.dispose();
            }
        });

        stream.getSaveButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String sn = stream.getShort_name().getText();
                String ln = stream.getLong_name().getText();
                String sp = stream.getSub_price().getText();
                System.out.println(sn + " ," + ln + ", " + sp);
                /* Execute the testreader*/
                String[] tokens = {"create_stream", sn, ln, sp};
                try {
                    caseScanner.processInstructions(tokens);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                stream.setEmpty("");
                ndframe.dispose();
            }
        });
        stream.getCancelButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.dispose();
            }
        });

        nextMonthButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                /* Execute the testreader*/
                String[] tokens = {"next_month"};
                try {
                    caseScanner.processInstructions(tokens);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                currentDate.setText("Current Time: " + TestCaseReader.getMonthTimeStamp() + "/" + TestCaseReader.getYearTimeStamp());
            }
        });

        offm.getSaveButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String ss = offm.getStream().getText();
                String movie = offm.getMovie().getText();
                String year = offm.getYear().getText();
                System.out.println("Streaming service: "+ss+", movie name: "+ movie + ", year: " + year);
                /* Execute the testreader*/
                String[] tokens = {"offer_movie", ss, movie, year};
                try {
                    caseScanner.processInstructions(tokens);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                offm.setEmpty("");
                ndframe.dispose();
            }
        });
        offm.getCancelButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.dispose();
            }
        });

        offppv.getSaveButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String ss = offppv.getStream().getText();
                String ppv = offppv.getPpv_name().getText();
                String year = offppv.getYear().getText();
                String vp = offppv.getView_price().getText();
                System.out.println("Streaming service: "+ss+", PPV name: "+ ppv + ", year: " + year + ", view price: "+vp);
                /* Execute the testreader*/
                String[] tokens = {"offer_ppv", ss, ppv, year, vp};
                try {
                    caseScanner.processInstructions(tokens);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                offppv.setEmpty("");
                ndframe.dispose();
            }
        });

        offppv.getCancelButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.dispose();
            }
        });

        watche.getSaveButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String dg = watche.getDemo_group().getText();
                String per = watche.getPercentage().getText();
                String ss = watche.getStream().getText();
                String en = watche.getEvent().getText();
                String year = watche.getYear().getText();
                System.out.println("Demo Group: " + dg + "Percentage: " + per +", Streaming service: "+ss+", Event name: "+ en + ", year: " + year);
                /* Execute the testreader*/
                String[] tokens = {"watch_event", dg, per, ss, en, year};
                try {
                    caseScanner.processInstructions(tokens);
//                    System.out.println(caseScanner.getStringoutput()[0]);
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
                watche.setEmpty("");
                ndframe.dispose();
            }
        });

        watche.getCancelButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.dispose();
            }
        });

        /* Data includes: demo, stream, and studio*/
        displayd.getDisplayButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                displayd.settableData(new Object[][]{{"",""},{"",""}});
                String sel = displayd.getDisplaySelections().getSelection().getActionCommand();
                String sn = displayd.getShort_name().getText();
                System.out.println("selected: "  +sel+ " with short name: " + sn);
                /* Execute the testreader*/
                String[] tokens = {"display_" + sel, sn};
                try {
                    caseScanner.processInstructions(tokens);
                    displayd.settableData(caseScanner.getStringoutput());
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
                /* Close current panel*/
            }
        });

        showFinancialDataButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ndframe.setContentPane(displayf.getDisplayPanel());
                ndframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                ndframe.pack();
                ndframe.setSize(600, 500);
                ndframe.setVisible(true);
            }
        });

        displayf.getDisplayButton().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String sel = displayf.getDisplaySelections().getSelection().getActionCommand();
                String sn = displayf.getShortnameTextField().getText();
                System.out.println("selected: "  +sel);
                String[] tokens = {sel, sn};
                try {
                    System.out.println("Enter Case Scanner. Begin to process instructions");
                    caseScanner.processInstructions(tokens);
                    System.out.println("Get data from Scanner:");
//                    System.out.println("Data: "+ caseScanner.getStringoutput()[0][0].toString());
                    displayf.settableData(caseScanner.getStringoutput());
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                } catch (ClassNotFoundException classNotFoundException) {
                    classNotFoundException.printStackTrace();
                }
            }
        });

    }
}

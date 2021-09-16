package gatech;

import javax.swing.*;
import javax.swing.table.AbstractTableModel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class displayData {
    private JPanel displayPanel;
    private JRadioButton demographicGroupRadioButton;
    private JRadioButton streamRadioButton;
    private JRadioButton studioRadioButton;
    private JTable dataTable;
    private JTextField short_name;
    private JButton displayButton;
    private ButtonGroup selections  =new ButtonGroup();
    private MyTableModel tableModel = new MyTableModel();

    public ButtonGroup getDisplaySelections() {
        demographicGroupRadioButton.setActionCommand("demo");
//        demographicGroupRadioButton.addActionListener();
        streamRadioButton.setActionCommand("stream");
        studioRadioButton.setActionCommand("studio");
        selections.add(demographicGroupRadioButton);
        selections.add(streamRadioButton);
        selections.add(studioRadioButton);

        return selections;
    }

    public JButton getDisplayButton() {
        return displayButton;
    }

    public JRadioButton getDemographicGroupRadioButton() {
        return demographicGroupRadioButton;
    }

    public JRadioButton getStreamRadioButton() {
        return streamRadioButton;
    }

    public JRadioButton getStudioRadioButton() {
        return studioRadioButton;
    }

    public JTextField getShort_name() {
        return short_name;
    }

    public JPanel getDisplayPanel() {
        tableModel.setColumnNames(new String[]{"", ""});
        tableModel.setData(new Object[][]{{"",""},{"",""}});
        dataTable.setModel(tableModel);
        return displayPanel;
    }

    public void settableData(Object[][] objectArr){
        tableModel.setData(objectArr);
        tableModel.fireTableDataChanged();
    }

    class MyTableModel extends AbstractTableModel {
        private String[] columnNames = {"First Name",
                "Last Name",
                "Sport",
                "# of Years",
                "Vegetarian"};

        private Object[][] data = {
                {"Kathy", "Smith",
                        "Snowboarding", "test1", "test2"},

        };

        public void setColumnNames(String[] columnNames) {
            this.columnNames = columnNames;
        }

//        public void setData(Object[][] data) {
//            this.data = data;
//        }
        public void setData(Object[][] data) {
            this.data = data;
        }

        public int getColumnCount() {
            return columnNames.length;
        }

        public int getRowCount() {
            return data.length;
        }

        public String getColumnName(int col) {
            return columnNames[col];
        }

        public Object getValueAt(int row, int col) {
            return data[row][col];
        }

        /*
         * JTable uses this method to determine the default renderer/
         * editor for each cell.  If we didn't implement this method,
         * then the last column would contain text ("true"/"false"),
         * rather than a check box.
         */
        public Class getColumnClass(int c) {
            return getValueAt(0, c).getClass();
        }

        /*
         * Don't need to implement this method unless your table's
         * editable.
         */
        public boolean isCellEditable(int row, int col) {
            //Note that the data/cell address is constant,
            //no matter where the cell appears onscreen.
            if (col < 2) {
                return false;
            } else {
                return true;
            }
        }

        /*
         * Don't need to implement this method unless your table's
         * data can change.
         */
        public void setValueAt(Object value, int row, int col) {
            data[row][col] = value;
            fireTableCellUpdated(row, col);
        }

    }





}



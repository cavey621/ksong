package gatech;

import javax.swing.*;
import javax.swing.table.AbstractTableModel;

public class displayFinancial {
    private JRadioButton demoSpendingHistoryRadioButton;
    private JRadioButton streamRevenueHistoryRadioButton;
    private JRadioButton studioEvenueHistoryRadioButton;
    private JButton displayButton;
    private JTable financialDataTable;
    private JPanel displayPanel;
    private JTextField shortnameTextField;

    private ButtonGroup selections  =new ButtonGroup();
    private displayFinancial.MyTableModel tableModel = new displayFinancial.MyTableModel();

    public JButton getDisplayButton() {
        return displayButton;
    }

    public JTextField getShortnameTextField() {
        return shortnameTextField;
    }

    public ButtonGroup getDisplaySelections() {
        demoSpendingHistoryRadioButton.setActionCommand("display_demo_spending_history");
//        demographicGroupRadioButton.addActionListener();
        streamRevenueHistoryRadioButton.setActionCommand("display_stream_revenue_history");
        studioEvenueHistoryRadioButton.setActionCommand("display_studio_revenue_history");
        selections.add(demoSpendingHistoryRadioButton);
        selections.add(streamRevenueHistoryRadioButton);
        selections.add(studioEvenueHistoryRadioButton);

        return selections;
    }
    public JPanel getDisplayPanel() {
        tableModel.setColumnNames(new String[]{"213", "1234"});
        tableModel.setData(new Object[][]{{"name","TEST"},{"size","test"}});
        financialDataTable.setModel(tableModel);
        return displayPanel;
    }

    public void settableData(Object[][] objectArr){
//        System.out.println("=============");
//        System.out.println(objectArr[0][0].toString());
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
                        "Snowboarding", new Integer(5), new Boolean(false)},
                {"John", "Doe",
                        "Rowing", new Integer(3), new Boolean(true)},
                {"Sue", "Black",
                        "Knitting", new Integer(2), new Boolean(false)},
                {"Jane", "White",
                        "Speed reading", new Integer(20), new Boolean(true)},
                {"Joe", "Brown",
                        "Pool", new Integer(10), new Boolean(false)}
        };

        public void setColumnNames(String[] columnNames) {
            this.columnNames = columnNames;
        }

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

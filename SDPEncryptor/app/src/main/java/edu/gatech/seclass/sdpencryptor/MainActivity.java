package edu.gatech.seclass.sdpencryptor;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import java.nio.charset.CharacterCodingException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class MainActivity extends AppCompatActivity {
    private EditText textDispatch;
    private EditText textArgument0;
    private EditText textArgument1;
    private TextView textEncodedDispatch;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textDispatch = (EditText) findViewById(R.id.dispatchID);
        textArgument0 = (EditText) findViewById(R.id.arg0ID);
        textArgument1 = (EditText) findViewById(R.id.arg1ID);
        textEncodedDispatch = (TextView) findViewById(R.id.encodedDispatchID);
    }
    public void handClick(View view) {
        if (view.getId() == R.id.encipherButtonID) {
            textEncodedDispatch.setText("");
            String result;
            String arg0 = textArgument0.getText().toString();
            String arg1 = textArgument1.getText().toString();
            String dispatch = textDispatch.getText().toString();
            if (!isValidDispatch(dispatch)) {
                textDispatch.setError("Invalid Dispatch");
            }
            if (!isValidArg0(arg0)) {
                textArgument0.setError("Invalid Argument 0");
            }
            if (!isValidArg1(arg1)) {
                textArgument1.setError("Invalid Argument 1");
            }
            if (isValidInput(dispatch,arg0,arg1)) {
                int a = Integer.parseInt(arg0);
                int b = Integer.parseInt(arg1);
                result = getEncodedMsg(dispatch, a, b);
                textEncodedDispatch.setText(result);
            }
        }
    }

    private boolean isValidInput(String dispatch, String arg0, String arg1) {
        return isValidDispatch(dispatch) && isValidArg0(arg0) && isValidArg1(arg1);
    }

    private boolean isValidDispatch(String dispatch) {
        if (dispatch.equals("")) return false;
        for (char c : dispatch.toCharArray()) {
            if (Character.isLetter(c))
                return true;
        }
        return false;
    }

    private boolean isValidArg0(String arg0) {
        if (arg0.equals("")) return false;
        for (char c : arg0.toCharArray()) {
            if (!Character.isDigit(c))
                return false;
        }
        int a = Integer.parseInt(arg0);
        Set<Integer> coprimes = new HashSet<>(Arrays.asList(1,3,5,7,9,11,15,17,19,21,23,25));
        if (!coprimes.contains(a)) return false;
        return true;
    }

    private boolean isValidArg1(String arg1) {
        if (arg1.equals("")) return false;
        for (char c : arg1.toCharArray()) {
            if (!Character.isDigit(c))
                return false;
        }
        int b = Integer.parseInt(arg1);
        if (b < 1 || b >=26)  return false;
        return true;
    }


    private String getEncodedMsg(String dispatch, int a, int b){
        StringBuilder dispatchSB = new StringBuilder(dispatch);
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < dispatchSB.length(); i++) {
            char c = dispatchSB.charAt(i);
            if (Character.isLetter(c)){
                int x = Character.toUpperCase(c) - 65;
                int y = (a * x + b) % 26;
                char encodedLetter = (char) (65 + y); // in Upper case
                if (Character.isUpperCase(c)) {
                    encodedLetter = Character.toLowerCase(encodedLetter);
                }
                c = encodedLetter;
            }
            res.append(c);
        }
        return res.toString();
    }


}
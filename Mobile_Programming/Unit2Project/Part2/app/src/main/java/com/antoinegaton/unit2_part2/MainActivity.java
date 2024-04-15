package com.antoinegaton.unit2_part2;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText num1EditText, num2EditText;
    TextView resultTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        num1EditText = findViewById(R.id.num1);
        num2EditText = findViewById(R.id.num2);
        resultTextView = findViewById(R.id.tvResult);

        Button btnMod = findViewById(R.id.btnMod);
        Button btnAdd = findViewById(R.id.btnAdd);
        Button btnSubtract = findViewById(R.id.btnSubtract);
        Button btnDivide = findViewById(R.id.btnDivide);
        Button btnPower = findViewById(R.id.btnPower);

        btnMod.setOnClickListener(v -> calculateOperation('%'));
        btnAdd.setOnClickListener(v -> calculateOperation('+'));
        btnSubtract.setOnClickListener(v -> calculateOperation('-'));
        btnDivide.setOnClickListener(v -> calculateOperation('/'));
        btnPower.setOnClickListener(v -> calculateOperation('^'));
    }

    private void calculateOperation(char operation) {
        String num1String = num1EditText.getText().toString();
        String num2String = num2EditText.getText().toString();
        double num1, num2, result;

        if(num1String.isEmpty() || num2String.isEmpty()) {
            Toast.makeText(this, "Please enter both numbers.", Toast.LENGTH_SHORT).show();
            return;
        }

        try {
            num1 = Double.parseDouble(num1String);
            num2 = Double.parseDouble(num2String);
        } catch (NumberFormatException e) {
            Toast.makeText(this, "Invalid number entered.", Toast.LENGTH_SHORT).show();
            return;
        }

        switch (operation) {
            case '%':
                // Handling for mod operation
                result = num1 % num2;
                resultTextView.setText(String.format("%s mod %s = %s", num1String, num2String, result));
                break;
            case '+':
                result = num1 + num2;
                resultTextView.setText(String.format("%s + %s = %s", num1String, num2String, result));
                break;
            case '-':
                result = num1 - num2;
                resultTextView.setText(String.format("%s - %s = %s", num1String, num2String, result));
                break;
            case '/':
                if (num2 == 0) {
                    Toast.makeText(this, "Cannot divide by zero.", Toast.LENGTH_SHORT).show();
                    return;
                }
                result = num1 / num2;
                resultTextView.setText(String.format("%s / %s = %s", num1String, num2String, result));
                break;
            case '^':
                result = Math.pow(num1, num2);
                resultTextView.setText(String.format("%s ^ %s = %s", num1String, num2String, result));
                break;
            default:
                Toast.makeText(this, "Unknown operation.", Toast.LENGTH_SHORT).show();
                break;
        }
    }
}

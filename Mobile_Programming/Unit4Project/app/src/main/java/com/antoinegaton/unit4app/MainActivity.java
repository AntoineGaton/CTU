package com.antoinegaton.unit4app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText editTextString1, editTextString2;
    private TextView textViewResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editTextString1 = findViewById(R.id.editTextString1);
        editTextString2 = findViewById(R.id.editTextString2);
        textViewResult = findViewById(R.id.textViewResult);
        Button buttonAdd = findViewById(R.id.buttonAdd);
        Button buttonCompare = findViewById(R.id.buttonCompare);
        Button buttonCountVowels = findViewById(R.id.buttonCountVowels);

        buttonAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String result = editTextString1.getText().toString() + editTextString2.getText().toString();
                textViewResult.setText(result);
            }
        });

        buttonCompare.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str1 = editTextString1.getText().toString();
                String str2 = editTextString2.getText().toString();
                if (str1.equals(str2)) {
                    textViewResult.setText("Matching");
                } else {
                    textViewResult.setText("Not matching");
                }
            }
        });

        buttonCountVowels.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String combined = editTextString1.getText().toString() + editTextString2.getText().toString();
                int count = 0;
                for (int i = 0; i < combined.length(); i++) {
                    char ch = combined.charAt(i);
                    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
                            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                        count++;
                    }
                }
                textViewResult.setText("Total vowels: " + count);
            }
        });
    }
}

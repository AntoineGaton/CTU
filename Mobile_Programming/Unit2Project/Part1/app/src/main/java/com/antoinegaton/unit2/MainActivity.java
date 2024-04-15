package com.antoinegaton.unit2;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;
import android.widget.EditText;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // Initialize UI components
        EditText customerName = findViewById(R.id.Customer_Name_Input);
        EditText customerID = findViewById(R.id.Customer_ID_Input);
        EditText customerAddress = findViewById(R.id.Customer_Address_Input);
        Button submitButton = findViewById(R.id.Submit_Button);

        // Set the OnClickListener for the submit button
        submitButton.setOnClickListener(v -> {
            // Get the text from each EditText
            String name = customerName.getText().toString().trim();
            String id = customerID.getText().toString().trim();
            String address = customerAddress.getText().toString().trim();

            // Validation logic
            // Check if any of the fields are empty
            if (name.isEmpty() || id.isEmpty() || address.isEmpty()) {
                Toast.makeText(MainActivity.this, "All inputs required.", Toast.LENGTH_SHORT).show();
            } else {
                // Ensure Customer Name contains no numeric characters
                if (!name.matches("[a-zA-Z ]+")) {
                    Toast.makeText(MainActivity.this, "Name can only contain letters and spaces.", Toast.LENGTH_SHORT).show();
                }
                try {
                    // Parse the Customer ID and check if it's between 0 and 1000
                    int customerId = Integer.parseInt(id);
                    if (customerId < 0 || customerId > 1000) {
                        Toast.makeText(MainActivity.this, "ID must be a value between 0 and 1000...", Toast.LENGTH_SHORT).show();
                    } else {
                        Intent intent = new Intent(MainActivity.this, MainActivity2.class);
                        intent.putExtra("CustomerName", name);
                        intent.putExtra("CustomerID", id);
                        intent.putExtra("CustomerAddress", address);
                        startActivity(intent);
                    }
                } catch (NumberFormatException e) {
                    // Catch invalid number input for ID
                    Toast.makeText(MainActivity.this, "Please enter a valid number for ID.", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
package com.antoinegaton.unit2;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity3 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        // Initialize UI components
        TextView customerNameTextView = findViewById(R.id.customerName);
        TextView customerIDTextView = findViewById(R.id.customerID);
        TextView customerAddressTextView = findViewById(R.id.customerAddress);
        TextView orderIDTextView = findViewById(R.id.orderID);
        TextView orderNameTextView = findViewById(R.id.orderName);
        TextView orderQuantityTextView = findViewById(R.id.orderQuantity);
        TextView orderFulfilledByTextView = findViewById(R.id.orderFulfilledBy);
        Button backButton = findViewById(R.id.backButton); // The new back button

        // Get the data from the intent
        Intent intent = getIntent();
        if (intent != null) {
            String customerName = intent.getStringExtra("CustomerName");
            String customerID = intent.getStringExtra("CustomerID");
            String customerAddress = intent.getStringExtra("CustomerAddress");
            String orderID = intent.getStringExtra("OrderID");
            String orderName = intent.getStringExtra("OrderName");
            String orderQuantity = intent.getStringExtra("OrderQuantity");
            String orderFulfilledBy = intent.getStringExtra("OrderFulfilledBy");

            // Set the text to display the information
            customerNameTextView.setText("Customer Name: " + customerName);
            customerIDTextView.setText("Customer ID: " + customerID);
            customerAddressTextView.setText("Customer Address: " + customerAddress);
            orderIDTextView.setText("Order ID: " + orderID);
            orderNameTextView.setText("Order Name: " + orderName);
            orderQuantityTextView.setText("Order Quantity: " + orderQuantity);
            orderFulfilledByTextView.setText("Order Fulfilled By: " + orderFulfilledBy);
        }

        // Set onClickListener for the back button
        backButton.setOnClickListener(v -> {
            // Navigate back to MainActivity1
            Intent backIntent = new Intent(MainActivity3.this, MainActivity.class);
            backIntent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK);
            startActivity(backIntent);
            finish(); // If you want to close this activity
        });
    }
}

package com.antoinegaton.unit2;

import android.app.DatePickerDialog;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Calendar;
import java.util.Locale;

public class MainActivity2 extends AppCompatActivity {

    private EditText orderID;
    private EditText orderName;
    private EditText orderQuantity;
    private EditText orderFulfilledBy;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        // Initialize UI components
        orderID = findViewById(R.id.Customer_Order_ID_Input);
        orderName = findViewById(R.id.Order_Name_Input);
        orderQuantity = findViewById(R.id.Order_Quantity_Input);
        orderFulfilledBy = findViewById(R.id.Order_FulfilledBy_Input);
        Button submitButton = findViewById(R.id.Next_Button);

        // Set up the 'Order Fulfilled By' EditText as a date picker
        orderFulfilledBy.setOnClickListener(v -> showDatePickerDialog());

        // Get the data from MainActivity
        Intent intent = getIntent();
        String customerName = intent.getStringExtra("CustomerName");
        String customerID = intent.getStringExtra("CustomerID");
        String customerAddress = intent.getStringExtra("CustomerAddress");

        // Set the OnClickListener for the submit button
        submitButton.setOnClickListener(v -> {
            // Collect the order information
            String orderIDStr = orderID.getText().toString().trim();
            String orderNameStr = orderName.getText().toString().trim();
            String orderQuantityStr = orderQuantity.getText().toString().trim();
            String orderFulfilledByStr = orderFulfilledBy.getText().toString().trim();

            // Validation logic here (not implemented)
            // Assuming validation is successful...

            // Create the intent for MainActivity3 and pass all data along
            Intent nextIntent = new Intent(MainActivity2.this, MainActivity3.class);
            nextIntent.putExtra("CustomerName", customerName);
            nextIntent.putExtra("CustomerID", customerID);
            nextIntent.putExtra("CustomerAddress", customerAddress);
            nextIntent.putExtra("OrderID", orderIDStr);
            nextIntent.putExtra("OrderName", orderNameStr);
            nextIntent.putExtra("OrderQuantity", orderQuantityStr);
            nextIntent.putExtra("OrderFulfilledBy", orderFulfilledByStr);

            startActivity(nextIntent);
        });
    }

    private void showDatePickerDialog() {
        // Use the current date as the default date in the picker
        final Calendar calendar = Calendar.getInstance();
        int year = calendar.get(Calendar.YEAR);
        int month = calendar.get(Calendar.MONTH);
        int day = calendar.get(Calendar.DAY_OF_MONTH);

        // Create and show a DatePickerDialog
        DatePickerDialog datePickerDialog = new DatePickerDialog(this,
                (view, year1, month1, dayOfMonth) -> {
                    // Format the date and set it as the text for orderFulfilledBy
                    String selectedDate = String.format(Locale.getDefault(), "%d-%02d-%02d", year1, month1 + 1, dayOfMonth);
                    orderFulfilledBy.setText(selectedDate);
                }, year, month, day);

        datePickerDialog.show();
    }
}
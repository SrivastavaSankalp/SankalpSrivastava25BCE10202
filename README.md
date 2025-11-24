# SankalpSrivastava25BCE10202
Hotel Management System 

This is a simple command-line interface (CLI) application written in Python to manage a basic hotel bill calculation, including room charges and restaurant orders.

Features-
1. Room Booking: Allows the user to select from five different room types (Standard, Business, Family, Deluxe, Suite) and specify the number of nights.
2. Food Ordering: Provides an interactive menu system to order multiple items from the restaurant menu.
3. Bill Calculation: Calculates the total cost, summing up room charges and food orders.
4. Receipt Generation: Prints a formatted bill summary, including customer name, phone, room details, itemized food orders, and the grand total.
5. QR Code Generation: Automatically generates a QR code image (qrcode.png) containing the calculated grand total for easy payment processing.

Prerequisites-
To run this script, you must have Python installed. You also need the QRcode library, which can be installed using pip.
!pip install QRcode

How to Run-
1. Save the provided code as a Python file (e.g., hotel_system.py).
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the script using the Python interpreter:
5. python hotel_system.py

Usage Example-
The script will guide you through the process:
1. Enter the Customer Name and Phone Number.
2. Select a Room Type (1-5) and enter the duration of stay (in nights).
   When prompted, enter 'yes' to order food or 'no' to proceed to the final bill.
3. If ordering food, select the item number and quantity. You can repeat this step multiple times.
4. Once you finish ordering food, the final bill will be displayed on the console, and a file named qrcode.png will be created in the same directory, showing the total amount due.

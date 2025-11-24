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
   
Sample output images
1-
<img width="547" height="866" alt="image" src="https://github.com/user-attachments/assets/7ba22ecb-0cd7-4ae4-8c43-317305da0215" />
<img width="316" height="341" alt="image" src="https://github.com/user-attachments/assets/72ca2bad-feb2-4102-b289-a853c8c59111" />
2-
<img width="716" height="1007" alt="image" src="https://github.com/user-attachments/assets/3a89f0e3-ca22-47db-b235-4dae448e281a" />
<img width="657" height="477" alt="image" src="https://github.com/user-attachments/assets/c0d141e8-f218-4c4c-a1bd-cfaddd06ded7" />
<img width="319" height="325" alt="image" src="https://github.com/user-attachments/assets/fbae6431-2699-4742-9dcd-8714939413a3" />

Hotel Bill Management System 
1. Problem Statement
Manual calculation of hotel bills, which includes varying room charges, duration of stay, and fluctuating restaurant orders, 
is prone to human error and can lead to disputes or operational delays at checkout. There is a need for a simple, reliable, and 
instant console-based application that automates the calculation of the total charges and presents a transparent, itemized bill 
to the customer, including a quick method for digital payment via QR code.

2. Scope of the Project
The project scope is focused on the core transaction process: billing.
Room selection and calculation based on fixed daily rates and duration of stay.
Interactive food/restaurant order processing and calculation.
Generation of a comprehensive, itemized final bill summary.
Generation of a QR code based on the final grand total for immediate payment (Requires the qrcode library).

3. Target Users

The system is designed primarily for:
-Hotel Reception/Staff
 to Rapidly calculate, finalize, and present a transparent bill to the customer at checkout, minimizing calculation errors.
-Guests
 to Review an itemized breakdown of their charges (room and food) and use the generated QR code for immediate, simplified payment.

4. High-Level Features

The application provides the following key functions:
Customer Data Capture: Collects essential customer details (Name, Phone Number) at the start of the billing process.
Room Charge Calculation: Allows the user to select from defined room types (e.g., Standard, Deluxe, Suite) and calculates the total room charge based on the number of nights.
Interactive Food Ordering: Presents a detailed restaurant menu and allows the user to iteratively add multiple food items with specified quantities.
Itemized Bill Generation: Calculates the subtotal for rooms and food, and sums them up to determine the Grand Total.
QR Code Payment Generation: Utilizes the qrcode library to encode the Grand Total amount into a .png image file, enabling quick digital payment by the guest.

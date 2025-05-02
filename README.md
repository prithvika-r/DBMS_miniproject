🏥 Medical Shop Management System
A mini project built using Python (Tkinter) and MySQL to manage a medical shop's operations including customer management, medicine inventory, billing, and viewing stock or bill details.

📁 Project Structure

medical_shop/
├── db_config.py            # MySQL connection setup
├── create_tables.sql       # SQL for tables, views, triggers, assertions
├── main.py                 # Main GUI launcher
├── medicine_mgmt.py        # Add medicine functionality
├── customer_mgmt.py        # Add customer functionality
├── billing.py              # Create bill functionality
├── view_data.py            # View stock and bills
└── README.md               # Project documentation

🛠 Technologies Used
Frontend: Python Tkinter

Backend: MySQL

Connector: mysql-connector-python

🗃 Database Features
Tables: Medicine, Customer, Bill, Bill_Items

Views:

Available_Medicines – shows non-expired medicines in stock

Bill_Details – shows complete bill breakdown

Triggers:

Prevent billing expired medicine

Auto-update stock after billing

Assertions (simulated):

No negative stock

Positive quantity on billing

✅ Features
Add new medicines and track expiry

Manage customers with contact details

Generate bills and auto-update medicine stock

View current stock and detailed bills

Validations via SQL constraints and triggers

⚙️ Setup Instructions
Install Python dependencies:


pip install mysql-connector-python
Create database and tables:

Open MySQL

Run create_tables.sql

Update db_config.py: Replace with your MySQL username/password.

Run the app:
python main.py

DBMS Mini Project 
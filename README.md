# 🏥 Medical Shop Management System

A desktop-based **Medical Shop Management System** developed using **Python Tkinter and MySQL** to automate pharmacy operations including medicine inventory management, customer management, billing, and stock tracking.

The project demonstrates database design concepts such as **tables, views, triggers, constraints, and CRUD operations**.

---

## 📌 Features

### 💊 Medicine Management
- Add and manage medicine details
- Track medicine expiry dates
- Maintain available stock information
- Prevent billing of expired medicines

### 👥 Customer Management
- Add and manage customer information
- Store customer contact details
- Maintain customer billing records

### 🧾 Billing System
- Generate customer bills
- Automatically update medicine stock after billing
- Validate medicine availability before billing

### 📊 Data Viewing
- View available medicines
- View detailed billing information
- Monitor inventory status

---

## 🛠 Technologies Used

### Frontend
- Python Tkinter

### Backend Database
- MySQL

### Python Libraries
- mysql-connector-python

---

## 🗃 Database Design

### Tables
- **Medicine**
  - Stores medicine details, price, quantity, expiry date

- **Customer**
  - Stores customer information

- **Bill**
  - Stores billing details

- **Bill_Items**
  - Stores individual medicines included in each bill

### Views
- **Available_Medicines**
  - Displays medicines that are not expired and currently available in stock

- **Bill_Details**
  - Provides complete bill breakdown including customer and medicine details

### Triggers
- Prevents billing of expired medicines
- Automatically updates stock after successful billing

### Constraints
- Prevents negative stock values
- Ensures positive billing quantities

---

## 📁 Project Structure
medical_shop/
│
├── db_config.py # MySQL database connection setup
├── create_tables.sql # Database schema, views, and triggers
├── main.py # Main Tkinter application launcher
├── medicine_mgmt.py # Medicine management module
├── customer_mgmt.py # Customer management module
├── billing.py # Billing operations
├── view_data.py # View stock and billing details
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1. Install required dependency

```bash
pip install mysql-connector-python
2. Setup Database
Open MySQL
Execute:
create_tables.sql
3. Configure Database Connection

Update db_config.py with your MySQL credentials:

host="localhost"
user="your_username"
password="your_password"
database="medical_shop"
4. Run Application
python main.py

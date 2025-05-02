import tkinter as tk
from tkinter import ttk
from db_config import get_connection

def configure_treeview_style():
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
    style.configure("Treeview", font=("Arial", 13))

def view_stock_ui():
    configure_treeview_style()

    win = tk.Toplevel()
    win.title("Available Medicines")
    win.geometry("1000x600")

    tree = ttk.Treeview(win, columns=('id', 'name', 'category', 'manufacturer', 'price', 'expiry', 'quantity'), show='headings')

    tree.heading('id', text='ID')
    tree.heading('name', text='Name')
    tree.heading('category', text='Category')
    tree.heading('manufacturer', text='Manufacturer')
    tree.heading('price', text='Price')
    tree.heading('expiry', text='Expiry Date')
    tree.heading('quantity', text='Stock Qty')

    tree.column('id', width=50)
    tree.column('name', width=150)
    tree.column('category', width=100)
    tree.column('manufacturer', width=120)
    tree.column('price', width=80)
    tree.column('expiry', width=100)
    tree.column('quantity', width=80)

    tree.pack(fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM available_medicines")
    for row in cursor.fetchall():
        tree.insert('', tk.END, values=row)
    cursor.close()
    conn.close()

def view_bills_ui():
    configure_treeview_style()

    win = tk.Toplevel()
    win.title("Bill Details")
    win.geometry("1000x600")

    tree = ttk.Treeview(win, columns=('bill_id', 'customer_id', 'medicine_id', 'quantity', 'price', 'total_amount', 'date'), show='headings')

    tree.heading('bill_id', text='Bill ID')
    tree.heading('customer_id', text='Customer ID')
    tree.heading('medicine_id', text='Medicine ID')
    tree.heading('quantity', text='Quantity')
    tree.heading('price', text='Price')
    tree.heading('total_amount', text='Total Amount')
    tree.heading('date', text='Date')

    tree.column('bill_id', width=50)
    tree.column('customer_id', width=100)
    tree.column('medicine_id', width=100)
    tree.column('quantity', width=80)
    tree.column('price', width=80)
    tree.column('total_amount', width=100)
    tree.column('date', width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.bill_id, b.customer_id, bi.medicine_id, bi.quantity, bi.price, b.total_amount, b.date
        FROM bill b
        JOIN bill_items bi ON b.bill_id = bi.bill_id
    """)
    for row in cursor.fetchall():
        tree.insert('', tk.END, values=row)
    cursor.close()
    conn.close()

def view_customers_ui():
    configure_treeview_style()

    win = tk.Toplevel()
    win.title("Customer Details")
    win.geometry("1000x600")

    tree = ttk.Treeview(win, columns=('customer_id', 'name', 'contact', 'address'), show='headings')

    tree.heading('customer_id', text='Customer ID')
    tree.heading('name', text='Name')
    tree.heading('contact', text='Contact')
    tree.heading('address', text='Address')

    tree.column('customer_id', width=50)
    tree.column('name', width=150)
    tree.column('contact', width=100)
    tree.column('address', width=200)

    tree.pack(fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    for row in cursor.fetchall():
        tree.insert('', tk.END, values=row)
    cursor.close()
    conn.close()

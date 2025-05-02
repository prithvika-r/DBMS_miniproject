import tkinter as tk
from tkinter import messagebox
from db_config import get_connection

font_label = ("Arial", 14)
font_entry = ("Arial", 14)
font_button = ("Arial", 14)

def add_customer_ui():
    def save_customer():
        conn = get_connection()
        cursor = conn.cursor()
        query = "insert into customer (name, phone, address) values (%s, %s, %s)"
        cursor.execute(query, (
            name_entry.get(), phone_entry.get(), address_entry.get()
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", " Customer added.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Add Customer")

    tk.Label(win, text="Name", font=font_label).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Phone", font=font_label).grid(row=1, column=0, padx=10, pady=5)
    tk.Label(win, text="Address", font=font_label).grid(row=2, column=0, padx=10, pady=5)

    name_entry = tk.Entry(win, font=font_entry)
    phone_entry = tk.Entry(win, font=font_entry)
    address_entry = tk.Entry(win, font=font_entry)

    name_entry.grid(row=0, column=1, padx=10, pady=5)
    phone_entry.grid(row=1, column=1, padx=10, pady=5)
    address_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(win, text="Save", font=font_button, command=save_customer).grid(row=3, columnspan=2, pady=10)


def update_customer_ui():
    def update_customer():
        customer_id = int(customer_id_entry.get())
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            update customer 
            set name = %s, phone = %s, address = %s
            where customer_id = %s
        """
        cursor.execute(query, (
            name_entry.get(), phone_entry.get(), address_entry.get(), customer_id
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", " Customer updated successfully.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Update Customer")

    tk.Label(win, text="Customer ID", font=font_label).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Name", font=font_label).grid(row=1, column=0, padx=10, pady=5)
    tk.Label(win, text="Phone", font=font_label).grid(row=2, column=0, padx=10, pady=5)
    tk.Label(win, text="Address", font=font_label).grid(row=3, column=0, padx=10, pady=5)

    customer_id_entry = tk.Entry(win, font=font_entry)
    name_entry = tk.Entry(win, font=font_entry)
    phone_entry = tk.Entry(win, font=font_entry)
    address_entry = tk.Entry(win, font=font_entry)

    customer_id_entry.grid(row=0, column=1, padx=10, pady=5)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    phone_entry.grid(row=2, column=1, padx=10, pady=5)
    address_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(win, text="Update", font=font_button, command=update_customer).grid(row=4, columnspan=2, pady=10)


def delete_customer_ui():
    def delete_customer():
        customer_id = int(customer_id_entry.get())
        conn = get_connection()
        cursor = conn.cursor()

        # Check if the customer has any related bills
        cursor.execute("SELECT COUNT(*) FROM bill WHERE customer_id = %s", (customer_id,))
        if cursor.fetchone()[0] > 0:
            messagebox.showerror("Error", "Cannot delete customer. Related bills exist.")
            return
        
        # If no related bills, proceed to delete the customer
        query = "DELETE FROM customer WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Customer deleted successfully.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Delete Customer")

    font_label = ("Arial", 12)
    font_entry = ("Arial", 12)
    font_button = ("Arial", 12, "bold")

    tk.Label(win, text="Customer ID", font=font_label).grid(row=0, column=0, padx=10, pady=5)

    customer_id_entry = tk.Entry(win, font=font_entry)
    customer_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(win, text="Delete", font=font_button, command=delete_customer).grid(row=1, columnspan=2, pady=10)

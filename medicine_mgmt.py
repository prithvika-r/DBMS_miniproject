import tkinter as tk
from tkinter import messagebox
from db_config import get_connection

# Font styles
font_label = ("Arial", 14)
font_entry = ("Arial", 14)
font_button = ("Arial", 14)

def add_medicine_ui():
    def save_medicine():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            insert into medicine (name, category, manufacturer, price, expiry_date, quantity_in_stock)
            values (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            name_entry.get(), category_entry.get(), manufacturer_entry.get(),
            float(price_entry.get()), expiry_entry.get(), int(stock_entry.get())
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Medicine added successfully.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Add Medicine")

    fields = ["Name", "Category", "Manufacturer", "Price", "Expiry (yyyy-mm-dd)", "Stock"]
    entries = []

    for i, field in enumerate(fields):
        tk.Label(win, text=field, font=font_label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(win, font=font_entry)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    name_entry, category_entry, manufacturer_entry, price_entry, expiry_entry, stock_entry = entries

    tk.Button(win, text="Save", font=font_button, command=save_medicine).grid(row=len(fields), columnspan=2, pady=10)


def update_medicine_ui():
    def update_medicine():
        medicine_id = int(medicine_id_entry.get())
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            update medicine 
            set name = %s, category = %s, manufacturer = %s, price = %s, expiry_date = %s, quantity_in_stock = %s
            where medicine_id = %s
        """
        cursor.execute(query, (
            name_entry.get(), category_entry.get(), manufacturer_entry.get(),
            float(price_entry.get()), expiry_entry.get(), int(stock_entry.get()), medicine_id
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Medicine updated successfully.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Update Medicine")

    labels = ["Medicine ID", "Name", "Category", "Manufacturer", "Price", "Expiry (yyyy-mm-dd)", "Stock"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(win, text=label, font=font_label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(win, font=font_entry)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    medicine_id_entry, name_entry, category_entry, manufacturer_entry, price_entry, expiry_entry, stock_entry = entries

    tk.Button(win, text="Update", font=font_button, command=update_medicine).grid(row=len(labels), columnspan=2, pady=10)


def delete_medicine_ui():
    def delete_medicine():
        medicine_id = int(medicine_id_entry.get())
        conn = get_connection()
        cursor = conn.cursor()
        query = "delete from medicine where medicine_id = %s"
        cursor.execute(query, (medicine_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Medicine deleted successfully.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Delete Medicine")

    tk.Label(win, text="Medicine ID", font=font_label).grid(row=0, column=0, padx=10, pady=5)

    medicine_id_entry = tk.Entry(win, font=font_entry)
    medicine_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(win, text="Delete", font=font_button, command=delete_medicine).grid(row=1, columnspan=2, pady=10)

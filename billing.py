import tkinter as tk
from tkinter import messagebox
from db_config import get_connection

def create_bill_ui():
    def generate_bill():
        try:
            customer_id = int(customer_entry.get())
            medicine_id = int(medicine_entry.get())
            qty = int(quantity_entry.get())

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("select price from medicine where medicine_id = %s", (medicine_id,))
            price = cursor.fetchone()[0]
            total = price * qty

            cursor.execute("insert into bill (customer_id, date, total_amount) values (%s, curdate(), %s)",
                        (customer_id, total))
            bill_id = cursor.lastrowid

            cursor.execute("insert into bill_items (bill_id, medicine_id, quantity, price) values (%s, %s, %s, %s)",
                        (bill_id, medicine_id, qty, price))

            conn.commit()
            messagebox.showinfo("Bill Created", f" Bill ID: {bill_id}\nTotal: ₹{total}")
            win.destroy()

        except Exception as e:
            if "cannot bill expired medicine" in str(e).lower():
                messagebox.showerror("Error", "❌ Cannot bill expired medicine!")
            else:
                messagebox.showerror("Database Error", str(e))

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    win = tk.Toplevel()
    win.title("Create Bill")
    font_label = ("Arial", 14)
    font_entry = ("Arial", 14)
    font_button = ("Arial", 14)
    tk.Label(win, text="Customer ID", font=font_label).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Medicine ID", font=font_label).grid(row=1, column=0, padx=10, pady=5)
    tk.Label(win, text="Quantity", font=font_label).grid(row=2, column=0, padx=10, pady=5)

    customer_entry = tk.Entry(win, font=font_entry)
    medicine_entry = tk.Entry(win, font=font_entry)
    quantity_entry = tk.Entry(win, font=font_entry)

    customer_entry.grid(row=0, column=1, padx=10, pady=5)
    medicine_entry.grid(row=1, column=1, padx=10, pady=5)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(win, text="Create Bill", font=font_button, command=generate_bill).grid(row=3, columnspan=2, pady=10)

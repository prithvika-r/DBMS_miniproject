import tkinter as tk
from medicine_mgmt import add_medicine_ui, update_medicine_ui, delete_medicine_ui
from customer_mgmt import add_customer_ui, update_customer_ui, delete_customer_ui
from billing import create_bill_ui
from view_data import view_stock_ui, view_bills_ui, view_customers_ui

root = tk.Tk()
root.title("Medical Shop Management")
root.geometry("900x900")

header_font = ("Arial", 20, "bold")
button_font = ("Arial", 14)

tk.Label(root, text="Medical Shop Management", font=header_font).pack(pady=20)

tk.Button(root, text="Add Medicine", width=25, font=button_font, command=add_medicine_ui).pack(pady=10)
tk.Button(root, text="Update Medicine", width=25, font=button_font, command=update_medicine_ui).pack(pady=10)
tk.Button(root, text="Delete Medicine", width=25, font=button_font, command=delete_medicine_ui).pack(pady=10)
tk.Button(root, text="View Stock", width=25, font=button_font, command=view_stock_ui).pack(pady=10)

tk.Button(root, text="Add Customer", width=25, font=button_font, command=add_customer_ui).pack(pady=10)
tk.Button(root, text="Update Customer", width=25, font=button_font, command=update_customer_ui).pack(pady=10)
tk.Button(root, text="Delete Customer", width=25, font=button_font, command=delete_customer_ui).pack(pady=10)
tk.Button(root, text="View Customers", width=25, font=button_font, command=view_customers_ui).pack(pady=10)

tk.Button(root, text="Create Bill", width=25, font=button_font, command=create_bill_ui).pack(pady=10)
tk.Button(root, text="View Bills", width=25, font=button_font, command=view_bills_ui).pack(pady=10)

root.mainloop()

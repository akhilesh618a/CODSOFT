# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk


# class ContactBook:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Contact Book")
#         self.root.geometry("500x500")
#         self.contacts = []

        
#         title = tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"))
#         title.pack(pady=10)

        
#         self.name_var = tk.StringVar()
#         self.phone_var = tk.StringVar()
#         self.email_var = tk.StringVar()

#         frame = tk.Frame(root)
#         frame.pack(pady=10)

#         tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e")
#         tk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1, padx=10)

#         tk.Label(frame, text="Phone:").grid(row=1, column=0, sticky="e")
#         tk.Entry(frame, textvariable=self.phone_var).grid(row=1, column=1, padx=10)

#         tk.Label(frame, text="Email:").grid(row=2, column=0, sticky="e")
#         tk.Entry(frame, textvariable=self.email_var).grid(row=2, column=1, padx=10)

        
#         button_frame = tk.Frame(root)
#         button_frame.pack(pady=10)

#         tk.Button(button_frame, text="Add Contact", command=self.add_contact, width=15).grid(row=0, column=0, padx=5)
#         tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, width=15).grid(row=0, column=1, padx=5)
#         tk.Button(button_frame, text="Clear Fields", command=self.clear_fields, width=15).grid(row=0, column=2, padx=5)

        
#         self.contact_list = ttk.Treeview(root, columns=("Name", "Phone", "Email"), show="headings", height=10)
#         self.contact_list.heading("Name", text="Name")
#         self.contact_list.heading("Phone", text="Phone")
#         self.contact_list.heading("Email", text="Email")
#         self.contact_list.pack(pady=10)

#     def add_contact(self):
#         name = self.name_var.get().strip()
#         phone = self.phone_var.get().strip()
#         email = self.email_var.get().strip()

#         if not name or not phone:
#             messagebox.showwarning("Input Error", "Name and phone are required!")
#             return

#         self.contacts.append((name, phone, email))
#         self.contact_list.insert("", "end", values=(name, phone, email))
#         self.clear_fields()

#     def delete_contact(self):
#         selected = self.contact_list.selection()
#         if not selected:
#             messagebox.showwarning("Select Contact", "No contact selected!")
#             return
#         for item in selected:
#             self.contact_list.delete(item)

#     def clear_fields(self):
#         self.name_var.set("")
#         self.phone_var.set("")
#         self.email_var.set("")



# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ContactBook(root)
#     root.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("520x520")
        self.root.configure(bg="#f0f4f7")  # light gray-blue background

        self.contacts = []

        # Title Label
        title = tk.Label(root, text="📒 Contact Book", font=("Arial", 20, "bold"), fg="#2c3e50", bg="#f0f4f7")
        title.pack(pady=10)

        # Input Fields
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        frame = tk.Frame(root, bg="#f0f4f7")
        frame.pack(pady=10)

        tk.Label(frame, text="Name:", bg="#f0f4f7", font=("Arial", 12)).grid(row=0, column=0, sticky="e")
        tk.Entry(frame, textvariable=self.name_var, width=30).grid(row=0, column=1, padx=10)

        tk.Label(frame, text="Phone:", bg="#f0f4f7", font=("Arial", 12)).grid(row=1, column=0, sticky="e")
        tk.Entry(frame, textvariable=self.phone_var, width=30).grid(row=1, column=1, padx=10)

        tk.Label(frame, text="Email:", bg="#f0f4f7", font=("Arial", 12)).grid(row=2, column=0, sticky="e")
        tk.Entry(frame, textvariable=self.email_var, width=30).grid(row=2, column=1, padx=10)

        # Buttons
        button_frame = tk.Frame(root, bg="#f0f4f7")
        button_frame.pack(pady=10)

        style = {"font": ("Arial", 10, "bold"), "width": 15, "fg": "white"}

        tk.Button(button_frame, text="Add Contact", command=self.add_contact,
                  bg="#27ae60", **style).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Contact", command=self.delete_contact,
                  bg="#c0392b", **style).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields,
                  bg="#2980b9", **style).grid(row=0, column=2, padx=5)

        # Contact List
        self.contact_list = ttk.Treeview(root, columns=("Name", "Phone", "Email"), show="headings", height=10)
        self.contact_list.heading("Name", text="Name")
        self.contact_list.heading("Phone", text="Phone")
        self.contact_list.heading("Email", text="Email")
        self.contact_list.pack(pady=10)

        # Style Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=25)
        style.map("Treeview", background=[('selected', '#a3d2ca')])
        self.contact_list.tag_configure('odd', background="#ecf0f1")
        self.contact_list.tag_configure('even', background="#d6eaf8")

        self.row_count = 0

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and phone are required!")
            return

        tag = 'even' if self.row_count % 2 == 0 else 'odd'
        self.contact_list.insert("", "end", values=(name, phone, email), tags=(tag,))
        self.row_count += 1
        self.clear_fields()

    def delete_contact(self):
        selected = self.contact_list.selection()
        if not selected:
            messagebox.showwarning("Select Contact", "No contact selected!")
            return
        for item in selected:
            self.contact_list.delete(item)

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")


# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()


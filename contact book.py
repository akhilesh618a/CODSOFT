import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk


contacts = []

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📒 Contact Book by Akhilesh")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffffff")  

        self.create_widgets()

    def create_widgets(self):
        
        title = tk.Label(self.root, text="Contact Book", font=("Arial", 20, "bold"),
                         bg="#ffffff", fg="#ff9933")  
        title.pack(pady=10)

        
        form_frame = tk.Frame(self.root, bg="#ffffff")
        form_frame.pack(pady=10)

        
        tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        tk.Label(form_frame, text="Phone:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        tk.Label(form_frame, text="Address:", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, sticky='e', padx=5, pady=5)

        self.name_entry = tk.Entry(form_frame, width=40)
        self.phone_entry = tk.Entry(form_frame, width=40)
        self.email_entry = tk.Entry(form_frame, width=40)
        self.address_entry = tk.Entry(form_frame, width=40)

        self.name_entry.grid(row=0, column=1, pady=5)
        self.phone_entry.grid(row=1, column=1, pady=5)
        self.email_entry.grid(row=2, column=1, pady=5)
        self.address_entry.grid(row=3, column=1, pady=5)

        
        btn_frame = tk.Frame(self.root, bg="#ffffff")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Contact", command=self.add_contact, bg="#28a745", fg="white", width=15).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="View Contacts", command=self.view_contacts, bg="#007bff", fg="white", width=15).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Search Contact", command=self.search_contact, bg="#fd7e14", fg="white", width=15).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Update Contact", command=self.update_contact, bg="#ffc107", fg="black", width=15).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Delete Contact", command=self.delete_contact, bg="#dc3545", fg="white", width=15).grid(row=2, column=0, columnspan=2, pady=5)

        
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email", "Address"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_form()
        self.view_contacts()

    def view_contacts(self):
        self.tree.delete(*self.tree.get_children())
        for contact in contacts:
            self.tree.insert('', tk.END, values=(contact["name"], contact["phone"], contact["email"], contact["address"]))

    def search_contact(self):
        name = simpledialog.askstring("Search", "Enter name to search:")
        if name:
            results = [c for c in contacts if c["name"].lower() == name.lower()]
            self.tree.delete(*self.tree.get_children())
            for contact in results:
                self.tree.insert('', tk.END, values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
            if not results:
                messagebox.showinfo("Not Found", "No contact found with that name.")

    def update_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a contact to update.")
            return

        item = self.tree.item(selected[0])
        old_name = item['values'][0]

        for contact in contacts:
            if contact["name"] == old_name:
                new_name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact["name"])
                new_phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=contact["phone"])
                new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact["email"])
                new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact["address"])
                
                contact["name"] = new_name or contact["name"]
                contact["phone"] = new_phone or contact["phone"]
                contact["email"] = new_email or contact["email"]
                contact["address"] = new_address or contact["address"]
                break

        self.view_contacts()
        messagebox.showinfo("Updated", "Contact updated successfully.")

    def delete_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a contact to delete.")
            return

        item = self.tree.item(selected[0])
        name = item['values'][0]

        confirm = messagebox.askyesno("Delete", f"Are you sure you want to delete {name}?")
        if confirm:
            global contacts
            contacts = [c for c in contacts if c["name"] != name]
            self.view_contacts()
            messagebox.showinfo("Deleted", "Contact deleted successfully.")

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

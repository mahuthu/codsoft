import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contact_list = []

        self.frame1 = tk.Frame(self.master)
        self.frame1.pack()

        self.label1 = tk.Label(self.frame1, text="Name:")
        self.label1.pack(side=tk.LEFT)

        self.entry1 = tk.Entry(self.frame1, width=10)
        self.entry1.pack(side=tk.LEFT)

        self.label2 = tk.Label(self.frame1, text="Phone:")
        self.label2.pack(side=tk.LEFT)

        self.entry2 = tk.Entry(self.frame1, width=10)
        self.entry2.pack(side=tk.LEFT)

        self.label3 = tk.Label(self.frame1, text="Email:")
        self.label3.pack(side=tk.LEFT)

        self.entry3 = tk.Entry(self.frame1, width=10)
        self.entry3.pack(side=tk.LEFT)

        self.button1 = tk.Button(self.frame1, text="Add Contact", command=self.add_contact)
        self.button1.pack(side=tk.LEFT)

        self.button2 = tk.Button(self.frame1, text="Delete Contact", command=self.delete_contact)
        self.button2.pack(side=tk.LEFT)

        self.button3 = tk.Button(self.frame1, text="Update Contact", command=self.update_contact)
        self.button3.pack(side=tk.LEFT)


        self.frame2 = tk.Frame(self.master)
        self.frame2.pack()

        self.listbox1 = tk.Listbox(self.frame2, height=10, width=50)
        self.listbox1.pack(side=tk.LEFT)

        self.scrollbar1 = tk.Scrollbar(self.frame2)
        self.scrollbar1.pack(side=tk.LEFT, fill=tk.Y)

        self.listbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)

        self.listbox1.bind('<<ListboxSelect>>', self.select_contact)
        self.load_contacts()

    def add_contact(self):
        name = self.entry1.get()
        phone = self.entry2.get()
        email = self.entry3.get()
        contact = Contact(name, phone, email)
        self.contact_list.append(contact)
        self.listbox1.insert(tk.END, contact)
        self.clear_entries()

    def delete_contact(self):
        try:
            index = self.listbox1.curselection()[0]
            self.listbox1.delete(index)
            self.contact_list.pop(index)
            self.clear_entries()
        except:
            messagebox.showwarning(title="Warning!", message="You must select a contact.")

    def update_contact(self):
        try:
            index = self.listbox1.curselection()[0]
            contact = self.contact_list[index]
            contact.name = self.entry1.get()
            contact.phone = self.entry2.get()
            contact.email = self.entry3.get()
            self.listbox1.delete(index)
            self.listbox1.insert(index, contact)
            self.clear_entries()
        except:
            messagebox.showwarning(title="Warning!", message="You must select a contact.")

    def select_contact(self, event):
        try:
            index = self.listbox1.curselection()[0]
            contact = self.contact_list[index]
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, contact.name)
            self.entry2.delete(0, tk.END)
            self.entry2.insert(0, contact.phone)
            self.entry3.delete(0, tk.END)
            self.entry3.insert(0, contact.email)
        except:
            pass

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as f:
                for line in f:
                    name, phone, email = line.split(",")
                    contact = Contact(name, phone, email)
                    self.contact_list.append(contact)
                    self.listbox1.insert(tk.END, contact)
        except:
            messagebox.showwarning(title="Warning!", message="Cannot find contacts.txt.")

    def save_contacts(self):    
        with open("contacts.txt", "w") as f:
            for contact in self.contact_list:
                f.write(contact.name + "," + contact.phone + "," + contact.email + "\n")

    def clear_entries(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)

    def __del__(self):
        self.save_contacts()

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return self.name + " " + self.phone + " " + self.email
    
    

def main():
    window = tk.Tk()
    app = ContactBookApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()




        

       


    
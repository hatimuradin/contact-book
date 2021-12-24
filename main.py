import tkinter as tk
from tkinter.constants import N
from src import DBHandler


class SimpleUI:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.window = tk.Tk()
        self.window.title("دفترچه تلفن")
        self.window.geometry("800x600")
        self.first_name_label = tk.Label(self.window, text="نام")
        self.last_name_label = tk.Label(self.window, text="نام خانوادگی")
        self.phone_label = tk.Label(self.window, text="شماره تلفن")
        self.email_label = tk.Label(self.window, text="ایمیل")

        self.contact_list = tk.Listbox(self.window, height=30, width=70)
        self.query_button = tk.Button(
            self.window,
            text="جستجو",
            fg="black",
            command=self.query,
        )
        self.entry_query = tk.Entry(self.window)
        self.entry_first_name = tk.Entry(self.window)
        self.entry_last_name = tk.Entry(self.window)
        self.entry_phone_number = tk.Entry(self.window)
        self.entry_email = tk.Entry(self.window)
        self.submit_button = tk.Button(
            self.window,
            text="جدید",
            fg="black",
            command=self.insert,
        )
        self.entry_delete = tk.Entry(self.window)
        self.delete_button = tk.Button(
            self.window,
            text="حذف",
            fg="red",
            command=self.delete,
        )
        # grid arrangement
        self.first_name_label.grid(row=0, column=0, sticky=tk.W)
        self.last_name_label.grid(row=0, column=1, sticky=tk.W)
        self.phone_label.grid(row=0, column=2, sticky=tk.W)
        self.email_label.grid(row=0, column=3, sticky=tk.W)
        self.entry_first_name.grid(row=1, column=0, sticky=tk.W)
        self.entry_last_name.grid(row=1, column=1, sticky=tk.W)
        self.entry_phone_number.grid(row=1, column=2)
        self.entry_email.grid(row=1, column=3)
        self.submit_button.grid(row=1, column=4)
        self.contact_list.grid(row=2, column=0, columnspan=3)
        self.entry_query.grid(row=2, column=3)
        self.query_button.grid(row=2, column=4)
        self.entry_delete.grid(row=3, column=0, columnspan=4, sticky=tk.W)
        self.delete_button.grid(row=3, column=1, sticky=tk.W)

        tk.mainloop()

    def query(self):
        query_text = self.entry_query.get()
        self.contact_list.delete(0, tk.END)
        all_items = self.db_handler.query(query_text)
        if len(all_items) == 0:
            self.contact_list.insert(tk.END, "موردی یافت نشد.")
        else:
            for item in all_items:
                pretty_text = (
                    f"{item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}"
                )
                self.contact_list.insert(tk.END, pretty_text)
        self.entry_query.delete(0, tk.END)

    def insert(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        phone_number = self.entry_phone_number.get()
        email = self.entry_email.get()
        self.db_handler.insert(first_name, last_name, phone_number, email)
        self.entry_query.delete(0, tk.END)
        self.query()
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_phone_number.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def delete(self):
        id = self.entry_delete.get()
        self.db_handler.delete(id)
        self.entry_query.delete(0, tk.END)
        self.query()
        self.entry_delete.delete(0, tk.END)


def main():
    db_handler = DBHandler()
    ui = SimpleUI(db_handler)


if __name__ == "__main__":
    main()

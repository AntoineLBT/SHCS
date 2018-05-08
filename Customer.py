from tkinter import *
from main import connect_db


class Customer:
    def __init__(self, root):
        self.array_cursor_top = []
        self.tick = None
        self.customer_id = None
        self.money = None
        self.last_name = None
        self.first_name = None
        self.contact = None
        self.array_cursor = []
        self.array_data = []
        self.data_label = None
        self.button_customer = None

        self.button_customer = Button(root, text='Client', command=self.display_customer)
        self.button_clean_customer = Button(root, text='Clean', command=self.clean_customer)

        self.button_customer.grid(row=0, column=0)
        self.button_clean_customer.grid(row=0, column=1)

    def clean_customer(self):
        # cleaning of top bar
        for i in range(0, len(self.array_cursor_top), 1):
            self.array_cursor_top[i].grid_forget()
        self.customer_id.grid_forget()
        self.money.grid_forget()
        self.first_name.grid_forget()
        self.last_name.grid_forget()
        self.contact.grid_forget()
        # cleaning of customer data
        for i in range(0, len(self.array_data), 1):
            self.array_data[i].grid_forget()
        # cleaning of separator
        for i in range(0, len(self.array_cursor), 1):
            self.array_cursor[i].grid_forget()

    def display_customer(self):
        for i in range(1, 11, 2):
            self.tick = Label(root, text="|")
            self.tick.grid(row=1, column=i)
            self.array_cursor_top.append(self.tick)

        self.customer_id = Label(root, text='N°client')
        self.money = Label(root, text='Cagnotte')
        self.last_name = Label(root, text='Nom')
        self.first_name = Label(root, text='Prénom')
        self.contact = Label(root, text='Contact')

        self.customer_id.grid(row=1, column=0)
        self.money.grid(row=1, column=2)
        self.last_name.grid(row=1, column=4)
        self.first_name.grid(row=1, column=6)
        self.contact.grid(row=1, column=8)

        connection, cursor = connect_db('db.db')

        cursor.execute("SELECT *FROM Customer")
        row = cursor.fetchall()
        i = 2
        self.array_cursor = []
        self.array_data = []
        for customer in row:
            j = 0
            k = 1
            for data in customer:

                self.data_label = Label(root, text=data)
                self.data_label.grid(row=i, column=j)
                self.array_data.append(self.data_label)

                self.tick = Label(root, text="|")
                self.tick.grid(row=i, column=k)
                self.array_cursor.append(self.tick)

                j += 2
                k += 2
            i += 1
        connection.close()


if __name__ == "__main__":
    root = Tk()
    root.title("SHCS")
    app = Customer(root)
    root.mainloop()

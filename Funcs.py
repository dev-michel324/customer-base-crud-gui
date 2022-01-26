from time import sleep
from tkinter import END, messagebox
from Db import Database

class Funcs(Database):
    def clear_all(self):
        self.entry_code.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_telephone.delete(0, END)
        self.entry_city.delete(0, END)

    def get_data(self):
        self.code = self.entry_code.get()
        self.name = self.entry_name.get()
        self.telephone = self.entry_telephone.get()
        self.city = self.entry_city.get()

    def select_list(self):
        self.listCli.delete(*self.listCli.get_children())
        self.connect_db()
        list = self.cursor.execute('''
            SELECT code, name_client, telephone, city FROM clients
            ORDER BY name_client ASc;
        ''')
        for i in list:
            self.listCli.insert('', END, values=i)
            print(i)
        self.disconnect_db()
        
    def search(self):
        self.get_data()
        def isNull(var):
            if var=='' or var.isspace():
                return 1
            return 0
        
        self.connect_db()
        self.listCli.delete(*self.listCli.get_children())
        self.entry_name.insert(END, '%')
        name = self.entry_name.get()
        self.cursor.execute('''
            SELECT * FROM clients WHERE name_client LIKE '%s' ORDER BY name_client ASC
            ''' % name)
        searchnameCli = self.cursor.fetchall()
        for i in searchnameCli:
            self.listCli.insert('', END, values=i)
            
        self.clear_all()
        self.disconnect_db()

    def add_client(self):
        self.get_data()
        if not self.name == '' and not self.name.isspace():
            if not self.telephone=='' and not self.telephone.isspace():
                if len(self.telephone) == 11:
                    if self.telephone.isdigit():
                        self.connect_db()
                        self.cursor.execute('''
                            INSERT INTO clients(name_client, telephone, city)
                            VALUES (?, ?, ?)''', (self.name, self.telephone, self.city))
                        self.conn.commit();
                        self.disconnect_db()
                        messagebox.showinfo('Added', 'Client Added')
                        self.select_list()
                        self.clear_all()
                    else:
                        messagebox.showerror('Error', 'The telephone field can only contain digits (numbers)!')
                else:
                    messagebox.showerror('Error', 'The number of numbers in the telephone field is invalid!')
            else:
                messagebox.showerror('Error', 'The telephone field is null!')
        else:
            messagebox.showerror('Error', 'The field name is null!')

    def onDoubleClick(self, event):
        self.clear_all()
        self.listCli.selection()

        for i in self.listCli.selection():
            col1, col2, col3, col4 = self.listCli.item(i, 'values')
            self.entry_code.insert(END, col1)
            self.entry_name.insert(END, col2)
            self.entry_telephone.insert(END, col3)
            self.entry_city.insert(END, col4)

    def update(self):
        self.get_data()
        self.connect_db()
        self.cursor.execute('''
            UPDATE clients SET name_client = ?, telephone = ?, city = ? WHERE code = ?
        ''', (self.name, self.telephone, self.city, self.code))
        self.conn.commit()
        self.disconnect_db()
        self.select_list()
        messagebox.showinfo('Success', 'Client updated!')
        self.clear_all()

    def remove(self):
        self.get_data()
        self.connect_db()
        if not self.code == '' and not self.code.isspace():
            self.cursor.execute('''
                DELETE FROM clients WHERE code = ?
            ''', (self.code))
            self.conn.commit()
            self.disconnect_db()
            self.clear_all()
            self.select_list()
        else:
            messagebox.showinfo('error', 'Select a client!')
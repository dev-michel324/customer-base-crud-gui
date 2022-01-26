from cgitb import text
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

from Funcs import Funcs
from Reports import Report

root = Tk()

class Application(Funcs, Report):
    def __init__(self):
        self.root = root
        self.display()
        self.framesOnDisplay()
        self.widgets_frame1()
        self.list_frame2()
        self.makeTables()
        self.select_list()
        self.menus()
        root.mainloop()

    def display(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1e3743')
        self.root.geometry('600x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=1000, height=600)
        self.root.minsize(width=500, height=400)
    
    def framesOnDisplay(self):
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame1.configure(
            background='#2a4552',
            bd=4,
            highlightbackground='gray',
            highlightthickness=1
        )
        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)
        self.frame2.configure(
            background='#2a4552',
            bd=4,
            highlightbackground='gray',
            highlightthickness=1
        )

    def widgets_frame1(self):
        # button clean
        self.btn_clear = Button(self.frame1, text='Clear', bd=1, bg='#157d8f', highlightbackground='#157d8f', command=self.clear_all)
        self.btn_clear.place(relx= 0.18, rely=0.06, relwidth=0.1, relheight=0.13)
        # button search
        self.btn_search = Button(self.frame1, text='Search', bd=1, bg='#157d8f', highlightbackground='#157d8f', command=self.search)
        self.btn_search.place(relx= 0.29, rely=0.06, relwidth=0.1, relheight=0.13)
        # button new
        self.btn_new = Button(self.frame1, text='New', bg='#25cc35', bd=1, highlightbackground='#25cc35', command=self.add_client)
        self.btn_new.place(relx= 0.66, rely=0.06, relwidth=0.1, relheight=0.13)
        # button update
        self.btn_update = Button(self.frame1, text='Update', bd=1, bg='#d9d321', highlightbackground='#d9d321', command=self.update)
        self.btn_update.place(relx= 0.77, rely=0.06, relwidth=0.1, relheight=0.13)
        # button remove
        self.btn_remove = Button(self.frame1, text='Remove', bg='#bf0f24', bd=1, highlightbackground='#bf0f24', command=self.remove)
        self.btn_remove.place(relx= 0.88, rely=0.06, relwidth=0.1, relheight=0.13)

        # btn to update the list
        self.btn_updateList = Button(self.frame1, text='Update List', bd=1, bg='#157d8f', highlightbackground='#157d8f', command=self.select_list)
        self.btn_updateList.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.13)

        
        ### Entrys frame1
        #lb and entry of code
        self.lb_code = Label(self.frame1, text='Code', bg='#2a4552', fg='white')
        self.lb_code.place(relx=0.02, rely=0)
        self.entry_code = Entry(self.frame1, bg='#dedede')
        self.entry_code.place(relx=0.02, rely=0.09, relwidth=0.13, relheight=0.1)

        #lb and entry of name
        self.lb_name = Label(self.frame1, text='Name', bg='#2a4552', fg='white')
        self.lb_name.place(relx=0.02, rely=0.35)
        self.entry_name = Entry(self.frame1, bg='#dedede')
        self.entry_name.place(relx=0.02, rely=0.44, relwidth=0.7, relheight=0.1)

        #lb and entry of telephone
        self.lb_telephone = Label(self.frame1, text='Telephone', bg='#2a4552', fg='white')
        self.lb_telephone.place(relx=0.02, rely=0.61)
        self.entry_telephone = Entry(self.frame1, bg='#dedede')
        self.entry_telephone.place(relx=0.02, rely=0.7, relwidth=0.45, relheight=0.1)

        #lb and entry of city
        self.lb_city = Label(self.frame1, text='City', bg='#2a4552', fg='white')
        self.lb_city.place(relx=0.5, rely=0.61)
        self.entry_city = Entry(self.frame1, bg='#dedede')
        self.entry_city.place(relx=0.5, rely=0.7, relwidth=0.45, relheight=0.1)

    def list_frame2(self):
        self.listCli = ttk.Treeview(self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listCli.heading('#0', text='')
        self.listCli.heading('#1', text='Code')
        self.listCli.heading('#2', text='Name')
        self.listCli.heading('#3', text='Telephone')
        self.listCli.heading('#4', text='City')

        self.listCli.column('#0', width=1)
        self.listCli.column('#1', width=80)
        self.listCli.column('#2', width=150)
        self.listCli.column('#3', width=150)
        self.listCli.column('#4', width=125)

        self.listCli.place(relx=0, rely=0, relwidth=0.98, relheight=1)

        self.scroolList = Scrollbar(self.frame2, orient='vertical')
        self.listCli.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.98, rely=0, relwidth=0.03, relheight=1)
        self.listCli.bind('<Double-1>', self.onDoubleClick)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        menubar.configure(bd=0, bg='#35647a')
        filemenu.configure(bd=1, bg='#437f9c')
        filemenu2.configure(bd=1, bg='#437f9c')

        def quit(): self.root.destroy()   

        menubar.add_cascade(label='Options', menu=filemenu)
        menubar.add_cascade(label='Reports', menu=filemenu2)

        filemenu.add_command(label='Quit', command=quit)
        filemenu.add_command(label='Clear Client', command=self.clear_all)
        filemenu2.add_command(label='customer report', command=self.generateReport)
        
if __name__ == '__main__':
    Application()
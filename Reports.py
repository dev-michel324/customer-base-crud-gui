from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

class Report():
    def printClient(self):
        webbrowser.open('client.pdf')

    def generateReport(self):
        self.c = canvas.Canvas('client.pdf')

        self.code = self.entry_code.get()
        self.name = self.entry_name.get()
        self.telephone = self.entry_telephone.get()
        self.city = self.entry_city.get()

        if not self.code=='' and not self.code.isspace():
            if not self.name=='' and not self.name.isspace():
                if len(self.telephone)==11 and self.telephone.isdigit():
                    if not self.city=='' and not self.city.isspace():
                        self.c.setFont('Helvetica-Bold', 22)
                        self.c.drawString(200, 780, 'Report of Client')

                        self.c.setFont('Helvetica-Bold', 13)
                        self.c.drawString(70, 700, 'Code: ')
                        self.c.drawString(70, 680, 'Name: ')
                        self.c.drawString(70, 660, 'Telephone: ')
                        self.c.drawString(70, 640, 'City: ')

                        self.c.setFont('Helvetica', 13)
                        self.c.drawString(150, 700, self.code)
                        self.c.drawString(150, 680, self.name)
                        self.c.drawString(150, 660, self.telephone)
                        self.c.drawString(150, 640, self.city)

                        self.c.showPage()
                        self.c.save()
                        self.printClient()
                    else:
                        messagebox.showerror('Error', 'The field city is null!')
                else:
                    messagebox.showerror('Error', 'The telephone field is invalid!')
            else:
                messagebox.showerror('Error', 'The field name is null!')
        else:
            messagebox.showerror('Error', 'The field code is null!')
from tkinter import *
from calculator import *
from tkinter import messagebox
import sys

class GUI():
    window = Tk()
    fileName = "data.txt"
    ents = []
    calc = Calculator()
    lab_names = ["Total Records:", "Percentage Completed:", "Percentage Goal:", "Updates Remaining:"]

    def __init__(self):
        self.makeform()
        try:
            self.calc.upload_from_file(self.fileName)
            self.update_fields()
        except ValueError as e:
            messagebox.showerror("Error", "The file %s contains invalid data: %s" %(self.fileName, e))
        mainloop()

    def update_fields(self):
        self.ents[0].delete(0, 'end')
        self.ents[0].insert(END, self.calc.total)
        self.ents[1].delete(0, 'end')
        self.ents[1].insert(END, ('%f' % self.calc.pUpdated).rstrip('0').rstrip('.'))
        self.ents[2].delete(0, 'end')
        self.ents[2].insert(END, ('%f' % self.calc.pGoal).rstrip('0').rstrip('.'))
        self.ents[3].configure(state="normal")
        self.ents[3].delete(0, 'end')
        self.ents[3].insert(END, self.calc.goal)
        self.ents[3].configure(state="readonly")

    def set_values(self):
        total = self.ents[0].get()
        pUpdated = self.ents[1].get()
        pGoal = self.ents[2].get()
        try:
            self.calc.set_values(total, pUpdated, pGoal)
        except ValueError as e:
            messagebox.showerror("Error", e)
            return False
        return True

    def calculate(self):
        if not self.set_values():
            return
        self.calc.calculate()
        self.ents[3].configure(state="normal")
        self.ents[3].delete(0, 'end')
        self.ents[3].insert(END, self.calc.goal)
        self.ents[3].configure(state="readonly")

    def save_and_quit(self):
        if not self.set_values():
            return
        self.calc.save_into_file(self.fileName)
        sys.exit()

    def makeform(self):
        self.window.title("Update Goal Calculator")
        self.window.geometry("300x170")
        for lab_name in self.lab_names:
            row = Frame(self.window)
            lab = Label(row, width=20, text=lab_name, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=LEFT, expand=YES, fill=X)
            self.ents.append(ent)

        self.update_fields()

        b1 = Button(self.window, text='Calculate', command=self.calculate)
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(self.window, text='Save&Quit', command=self.save_and_quit)
        b2.pack(side=RIGHT, padx=5, pady=5)

gui = GUI()
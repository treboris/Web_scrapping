import tkinter as tk
import os

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn1 = tk.Button(self, text="Avg Salary", command=self.open_diagram1)
        self.btn1.pack(side="left")

        self.btn2 = tk.Button(self, text="Diagram 2", command=self.open_diagram2)
        self.btn2.pack(side="left")

        self.btn3 = tk.Button(self, text="Diagram 3", command=self.open_diagram3)
        self.btn3.pack(side="left")

        self.btn4 = tk.Button(self, text="Diagram 4", command=self.open_diagram4)
        self.btn4.pack(side="left")

        self.btn5 = tk.Button(self, text="Diagram 5", command=self.open_diagram5)
        self.btn5.pack(side="left")

    def open_diagram1(self):
        os.system("python3 avg_salary.py")

    def open_diagram2(self):
        os.system("python location_diagram_hun.py")

    def open_diagram3(self):
        os.system("python ")

    def open_diagram4(self):
        os.system("python diagram4.py")

    def open_diagram5(self):
        os.system("python diagram5.py")

root = tk.Tk()
app = App(master=root)
app.mainloop()

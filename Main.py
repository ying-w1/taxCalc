import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Main:
    
    def __init__(self) -> None:
        self.window=tk.Tk()

         # Set size of window and title
        self.window.geometry("400x300") 
        self.window.title("Caculator")

        # Contents of window
        self.label = tk.Label(self.window, text="Tax Calculator FY2022-23",font=('Arial',18))
        self.label.pack(padx=20,pady=20)

        # Checkbox to select if super sacrifice
        self.check_state = tk.IntVar()
        self.checkButton = tk.Checkbutton(self.window, text = "I will make super contribution this FY",variable=self.check_state)
        self.checkButton.pack()

        # Enter income to calculate
        self.label2 = tk.Label(self.window, text="Taxable Income",font=('Arial',16))
        self.label2.pack()
        self.incomeEntry = tk.Entry(self.window)
        self.incomeButton = tk.Button(self.window, text="Submit", command=self.taxableIncome)
        self.incomeEntry.pack()
        self.incomeButton.pack(padx=10,pady=10)

        self.window.mainloop()
    
    def taxableIncome(self):
        tax = 0
        salary = int(self.incomeEntry.get())
        medRate = 0.02
        medLevy = salary * medRate
        
        if (salary <= 18200):
            tax = 0

        elif (salary > 18200) & (salary <= 45000):
            tax = ((salary-18200)*0.19) + medLevy

        elif (salary > 45000) & (salary <= 120000):
            tax = (5092 + (salary-45000)*0.325) + medLevy
        
        elif (salary > 120000) and (salary <= 180000):
            tax = (29467 + (salary-120000)*0.37) + medLevy
        
        else:
            tax = (51667 + (salary-180000)*0.45) + medLevy
        
        tax = int(tax)
        result = "Total tax payable for FY2022-23 is $"+ str('{:,}'.format(tax))

        messagebox.showinfo(title="taxable income", message=result)
    
    

Main()

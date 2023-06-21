import tkinter as tk
from tkinter import Label, Entry, StringVar, messagebox

class Main:

  def __init__(self) -> None:
    self.window = tk.Tk()

    # Set size of window and title
    self.window.geometry("400x300")
    self.window.title("Tax Calculator")

    # Contents of window
    self.label = tk.Label(self.window,
                          text="Tax Calculator FY2022-23",
                          font=('Arial', 18))
    self.label.grid(row=0, column=0)

    # Enter income to calculate
    self.label2 = tk.Label(self.window,
                           text="Taxable Income",
                           font=('Arial', 16))
    self.label2.grid(row=1, column=0)
    self.incomeEntry = tk.Entry(self.window)
    self.incomeEntry.grid(row=2, column=0)

    # Enter tax withheld
    self.label3 = tk.Label(self.window,
                           text="Tax Withheld",
                           font=('Arial', 16))
    self.label3.grid(row=3, column=0)
    self.withheldEntry = tk.Entry(self.window)
    self.withheldEntry.grid(row=4, column=0)

    # Submit button
    self.incomeButton = tk.Button(self.window,
                                  text="Calculate",
                                  command=self.taxableIncome)
    self.incomeButton.grid(row=5, column=0)

    # Text for checkers
    self.label = tk.Label(self.window,
                          text="Check if true:",
                          font=('Arial', 13))
    self.label.grid(row=8, column=0)
    
    # Checkbox to select if super sacrifice
    self.check_state = tk.IntVar()
    self.checkButton = tk.Checkbutton(
      self.window,
      text="Non concessional super contribution",
      variable=self.check_state)
    self.checkButton.grid(row=9, column=0,)

    # Checkbox to select if they have valid private health
    # UNcheck = 0
    # Check = 1
    self.check_pHealth = tk.IntVar()
    self.checkButton = tk.Checkbutton(
      self.window,
      text="Private health insurance with hospital cover",
      variable=self.check_pHealth)
    self.checkButton.grid(row=10, column=0)
    

    self.window.mainloop()

  def taxableIncome(self):
    tax = 0
    medRate = 0.02
    MLSurcharge = self.MLS()
    salary = int(self.incomeEntry.get())

    if len(self.withheldEntry.get()) == 0:
      taxWithheld = 0
    else:
      taxWithheld = int(self.withheldEntry.get())

    # Calculate medicare levy
    medLevy = salary * medRate

    # Calculate tax payable/refundable
    if salary <= 18200:
      tax = 0
    elif 18200 < salary <= 45000:
      tax = (salary - 18200) * 0.19 + medLevy
    elif 45000 < salary <= 120000:
      if self.check_pHealth.get() == 1:
        tax = (5092 + (salary - 45000) * 0.325) + medLevy
      else:
        tax = (5092 + (salary - 45000) * 0.325) + medLevy + MLSurcharge
    elif 120000 < salary <= 180000:
      if self.check_pHealth.get() == 1:
        tax = (29467 + (salary - 120000) * 0.37) + medLevy
      else:
        tax = (29467 + (salary - 120000) * 0.37) + medLevy + MLSurcharge
    else:
      if self.check_pHealth.get() == 1:
        tax = (51667 + (salary - 180000) * 0.45) + medLevy
      else:
        tax = (51667 + (salary - 180000) * 0.45) + medLevy + MLSurcharge

    tax = tax - taxWithheld
    tax = int(tax)

    if tax > 0:
      result = "Total tax payable for FY2022-23 is $" + str('{:,}'.format(tax))
    else:
      tax = tax * -1
      result = "Total tax refundable for FY2022-23 is $" + str(
        '{:,}'.format(tax))

    messagebox.showinfo(title="taxable income", message=result)

  def MLS(self):
    salary = int(self.incomeEntry.get())
    if salary <= 90000:
      return salary * 0
    elif 90001 <= salary <= 105000:
      return salary * 0.01
    elif 105001 <= salary <= 140000:
      return salary * 0.0125
    else:
      return salary * 0.015


Main()

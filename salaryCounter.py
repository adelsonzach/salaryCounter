from breezypythongui import EasyFrame

class SalaryCalc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Salary Calculator", width=300, height=200, resizable=False, background="lightgreen")

        # Input fields
        self.addLabel(text="Hourly Wage:", row=0, column=0)
        self.wageField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="No. of Hours Worked:", row=1, column=0)
        self.hoursField = self.addFloatField(value=0.0, row=1, column=1)

        # Button
        self.button = self.addButton(text="Calculate!", row=2, column=0, columnspan=2, command=self.calculate)

        # Output field
        self.addLabel(text="The employee's weekly salary is:", row=3, column=0)
        self.result = self.addFloatField(value=0.0, row=3, column=1, precision=2, state="readonly")

    def calculate(self):
        """Calculates weekly salary based on wage and hours input."""
        wage = self.wageField.getNumber()
        hours = self.hoursField.getNumber()
        weeklyPay = wage * hours
        self.result.setNumber(weeklyPay)

def main():
    SalaryCalc().mainloop()

if __name__ == '__main__':
    main()
from breezypythongui import EasyFrame

class SalaryCalc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Salary Calculator", width=300, height=200, resizable=False, background="lightgreen")

        # Input fields
        self.addLabel(text="Hourly Wage:", row=0, column=0)
        self.wageField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="No. of Hours Worked:", row=1, column=0)
        self.hoursField = self.addFloatField(value=0.0, row=1, column=1)

        # Button
        self.button = self.addButton(text="Calculate!", row=2, column=0, columnspan=2, command=self.calculate)

        # Output field
        self.addLabel(text="The employee's weekly salary is:", row=3, column=0)
        self.result = self.addFloatField(value=0.0, row=3, column=1, precision=2, state="readonly")

    def calculate(self):
        """Calculates weekly salary based on wage and hours input."""
        wage = self.wageField.getNumber()
        hours = self.hoursField.getNumber()
        weeklyPay = wage * hours
        self.result.setNumber(weeklyPay)

def main():
    SalaryCalc().mainloop()

if __name__ == '__main__':
    main()
#ZADE
class Bill:
    """
    Object that contains data about bill, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        

class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self,name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        """Counts amount to pay for flatmate."""
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = weight * bill.amount
        return to_pay


class PdfReport:
    """
    Creates a .pdf-file that contains data about
    flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """Generates a .pdf report"""
        pass


the_bill = Bill(amount=120, period="July 2023")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(f"{john.name} pays: ", john.pays(bill=the_bill, flatmate2=marry))
print(f"{marry.name} pays: ", marry.pays(bill=the_bill, flatmate2=john))

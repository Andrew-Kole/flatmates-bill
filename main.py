from flat import Bill, Flatmate
from reports import PdfReport, FileSharer
from dotenv import load_dotenv
import typing
import os

amount = float(input("Hey user, enter a bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

load_dotenv()
API_KEY: typing.Final = os.getenv("API_KEY")

file_sharer = FileSharer(filename=pdf_report.filename, api_key=API_KEY)
print(file_sharer.share())

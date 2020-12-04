"""A program that tracks personal expenses and income."""
# MSC 260 Fall 2020 Project 4
# Kortnee Reiss
# Declaration: I, Kortnee Reiss, am the sole author of this code, which
# was developed in accordance with the rules in the course syllabus 
import sys
import json
import datetime

counter=0
lis=[]
total = 0.00
while counter>=0:
    print("Expense tracker\n Spending categories: Housing, Transportation, Food, Utilities, Insurance, Misc(Miscellaneous)")
    print("Enter:\n  input[ex.10.00]\n  expenses[ex. 8.00]\n  date[ex.01/20/2020]\n  category\n  summary[Y/N]")
    summary = 0.00

    # Asks for input from user, including input, expenses, spending category,
    # date and summary.
    added = input("Enter input amount:  ")
    sub = input("Enter expenses amount: ")
    category = input("Enter spending category:  ")
    date = input("Enter date (mm/dd/yyyy):  ")
    summ = input("Return sum? Enter Y/N:    ")

    counter = counter+1
    
    #Creates a dictionary of entries to be added to the list
    entry = dict()          
    entry["input"] = added
    entry["expenses"] = sub
    entry["category"] = category
    entry["date"] = date
    summary = float(added) - float(sub)
    entry["earnings"] = summary
    total = total + summary
    if  summ == "Y":
        sumdate = input("Enter start date(mm/dd/yyyy): ")
        sumdate2 = input("Enter end date(mm/dd/yyyy):   ")
        a =0
        while a < len(lis):
            dicti = lis[a]
            for key, value in dicti.items():
                if key=="date":
                    if value == sumdate:
                        start = dicti["earnings"]
                    if value == sumdate2:
                        end = dicti["earnings"]
            a = a+1
        newsum = start+end
        print("\nSummary: ",newsum) 
    lis.append(entry)

    # Enter list onto a json file, and enter contents into the final variable 
    fil = open("expenses.json", "w",encoding="UTF-8")
    json.dump(lis,fil)
    fil.close()
    fil = open("expenses.json", "r", encoding="UTF-8")
    final =json.load(fil)
    fil.close()

    # Prints summary of entries
    print("\n")
    for a in final:
        for key, value in a.items():
            print(key, ":" , value)
    print("\n","\n")
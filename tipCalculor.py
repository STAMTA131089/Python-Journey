print("Welcome to the tip calculator!")

total_bill = float(input("what was the total bill? $"))
tip = int(input("How much tip % you would like to give? 10, 12,15 "))
people = int(input("How many people you want to split with"))

tip_percent = tip/100
a = total_bill * tip_percent
final_bill = total_bill + a

pay = final_bill/people
print(round(pay,2))

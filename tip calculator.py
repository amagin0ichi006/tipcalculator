print("welcome to tip calculator")
bill=float(input("what was the total bill?"))
percentage_tip = input("what percentage of tip would you like 10 12 15?")
tip_bill =float(bill/100 * bill + bill)
friends = int(input("how many people may share the bill?"))
split_bill = float(tip_bill) / friends
result = round(split_bill,2)
print("each person should pay:" , result)



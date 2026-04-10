print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill?"))

tip = ((bill/people) * (tip / 100))
final_bill = bill/people + tip

print(f"Each person should pay: ${round(final_bill,2)}")

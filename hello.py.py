# tip calculator
bill = int(input("enter bill amount"))
tip_percentage = int(input("enter tip percentage"))
tip = (bill * tip_percentage*1/100)
print("calculated tip is",tip)
total_bill = bill + tip 
print("total bill to be payed is $",total_bill)
 4
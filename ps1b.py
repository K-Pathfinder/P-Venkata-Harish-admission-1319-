Annual_Salary = float(input("Enter your annual salary: "))
Saving_rate = float(input("Enter the monthly saving rate in decimal: "))
Total_cost = float(input("Enter the cost of your dream house: "))
Semi_Annual_Salary = float(input("Enter the semi-annual raise (as decimal): "))
Down_payment = 0.25 * Total_cost
Current_saving = 0.0
Months = 0
Annual_return = 0.04
Monthly_return = Annual_return / 12
while Down_payment > Current_saving:
    Monthly_Salary = Annual_Salary / 12
    Current_saving += Current_saving * Monthly_return
    Current_saving += Monthly_Salary * Saving_rate
    Months += 1
    if Months % 6 == 0:
        Annual_Salary += Annual_Salary * Semi_Annual_Salary

print("Number of months:", Months)

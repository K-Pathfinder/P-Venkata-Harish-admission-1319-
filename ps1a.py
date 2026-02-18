Annual_Salary=float(input("enter your annual salary : ")) 
Saving_rate=float(input("enter the monthly saving rate in decimal : ")) 
Total_cost=float(input("enter the cost of your dream house : ")) 
Down_payment=0.25*Total_cost 
Current_saving=0.0 
Months=0
Monthly_Salary=0 
Annual_return=0.04 
Monthly_return=Annual_return/12 
while Down_payment>Current_saving: 
    Monthly_Salary=Annual_Salary/12 
    Current_saving+=Current_saving*Monthly_return 
    Current_saving+=Monthly_Salary*Saving_rate 
    Months+=1
print("Number of months:",Months)

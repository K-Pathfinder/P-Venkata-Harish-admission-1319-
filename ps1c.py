annual_salary = float(input("Enter your starting annual salary: "))
house_cost = 1000000.0
down_payment = house_cost * 0.25
current_savings = 0.0
annual_return = 0.04
months = 36
semiannual_raise = 0.07

epsilon = 100 
low = 0        
high = 10000   
steps = 0
best_saving_rate = 0.0

while True:
    steps += 1
    
    mid = (low + high) // 2
    rate = mid / 10000.0
    
    current_savings = 0.0
    monthly_salary = annual_salary / 12 
    
    for month in range(1, months + 1):
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_salary * rate
        
        if month % 6 == 0:
            monthly_salary += monthly_salary * semiannual_raise

    if abs(current_savings - down_payment) <= epsilon:
        best_saving_rate = rate
        break
    
    if current_savings < down_payment:
        low = mid 
    else:
        high = mid 
        
    if low >= high - 1:
        best_saving_rate = rate 
        break

if best_saving_rate !=0:
    print(f"Best saving rate: {best_saving_rate:.4f}")
    print(f"Steps in bisection search: {steps}")
else:
    print("It is not possible to pay the down payment in three years.")

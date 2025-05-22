# Mfano1
def calculate_salary_one(base_salary,bonus_rate):
   total_salary=base_salary*(1+bonus_rate)
   return total_salary

salary_1=900000
rate_1=0.6
print(calculate_salary_one(salary_1,rate_1))

# Mfano2
def calculate_salary_two(base_salary,bonus_rate=0.1):
   total_salary=base_salary*(1+bonus_rate)
   return total_salary
   

# Mfano2
salary_list=[100000,200000,300000,400000,500000]
calculated=[calculate_salary_two(x) for x in salary_list]
print(calculated)
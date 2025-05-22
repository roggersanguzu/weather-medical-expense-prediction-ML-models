
#Exercise1
salary_list=[100000,200000,300000,400000,500000]
calculated=[(lambda x: x*1.1)(salary) for salary in salary_list]
print(calculated)

# Exercise2
print((lambda x,y: x*y)(3,5))

# Exercise3
num=lambda a,b: a+b
print(num(34,5))


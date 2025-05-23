import random
import statistics
import numpy as np

x=[random.randint(5000,8900000) for _ in range (500000)]
print(x)

meanx=statistics.mean(x)
print(f'{meanx} is the Mean')


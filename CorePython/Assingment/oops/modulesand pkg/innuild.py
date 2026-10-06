# math ->it provides the matematic functions  or operetions
# import math
# math.sqrt(number )-> return sthe squre root of the number
# print(math.sqrt(16))
# 2. math.pow(base, exponent)->it will gives use  to the Power value
# print(math.pow(2,3))
# 3. Factorial-> math.factorial(it always accepts non negative intigers)
# print(math.factorial(5))
# 4.math.ceil() -> no matter how samll the decimal is it rounf uup the value properly
# print(math.ceil(12.8)) 
# print(math.floor(12.8)) #->it will goves prebious intiger
# print(math.pi)
# print(math.e)
# print(math.ceil(math.sin(90)))

import random
# random.randint(start,end)
# print(random.randint(1000,9999))
# random.choice(sequence)->it will choose random element from sequence  like list, touple, string
# f=["Apple","Oranges","Kivi","Mangos"]
# print(random.choice(f))

# random.random()->it will gives us any random value between 0.0 t0 1.0
# print(10000*random.random())
#  random.shuffle -> it woill work on the Shuffle the mutable sequence
# li=[12,18,7,34,45]
# random.shuffle(li)
# print(li)



# import datetime
# print(datetime.datetime.now())
# print(datetime.date.today())


import time
# print(time.time())
for i in range(1,30):
    print(i)
    time.sleep(1)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s_digit = str(number)[-1]
l_digit = int(s_digit)

if number < 0:
    l_digit *= -1
if l_digit > 5:
    print(f"Last digit of {str(number)} is {str(l_digit)} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {str(number)} is {str(l_digit)} and is 0")
elif l_digit < 6 and l_digit != 0:
    print(f"Last digit of {str(number)} is {str(l_digit)} and is less than 6 and not 0")

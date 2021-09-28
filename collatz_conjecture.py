import sys, time

# collatz conjecture
# 4
# 2
# 1
# loop
def simple_math(number):
    rules = {
        "odd": "multiply by 3 add 1",
        "even": "divide by 2"
    }
    
    while number:
        if (number % 2) == 0:
            number = number / 2
            print(int(number))
            time.sleep(1)
        else:
            number = number * 3 + 1
            print(int(number))
            time.sleep(1)

number = input("give me a number from 1 to 10\n")
simple_math(int(number))

# # print("Hello from lesson 9")# Recap 1: Dice Roll Simulator
# # Generate and print 3 random numbers between 1 and 6, followed
# # by an output of 'True' if all 3 numbers are either even or odd.

# # Example:
# # 1st number: 6
# # 2nd number: 4
# # 3rd number: 6
# # All numbers are even/odd: True

# # 1. Import the 'random' library
# # 2. Create 3 variables to hold a random number that is between
# #    1 and 6, generated using 'random.randint()'
# # 3. Using string concatenation, print the generated number for
# #    each of the 3 numbers
# # 4. Using the '%' and '==' operator, check if each number is
# #    divisible by 2 (remainder = 0)
# # 5. Using multiple '==' operators, a new variable 'all_even_odd'
# #    should be assigned 'True' if all 3 numbers are either all
# #    even or all odd numbers.
# # 6. Print if "All numbers are even/odd" is 'True' or 'False'

# import random

# num1 = random.randint(1, 6)
# num2 = random.randint(1, 6)
# num3 = random.randint(1, 6)
# print("first number:", num1)
# print("second number:", num2)
# print("third number:", num3)

# testnum1 = num1 % 2 == 0 
# testnum2 = num2 % 2 == 0
# testnum3 = num3 % 2 == 0

# print("all numbers are even/odd:", testnum1==testnum2==testnum3)


ask = int(input("HOW MANY DAYS DID U BORROW THE BOOK FOR"))

more = 25
less = 24

if ask < more:
    print("good boi")
else:
    print("REMEBER TO RETURN UR BOOK BOZO")


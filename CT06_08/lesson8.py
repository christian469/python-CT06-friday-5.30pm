# print("Hello from lesson 8")

# total = 1
# for i in range(1, 6):
#     number = int(input("what is number #" + str(i) + "? "))
#     total = total * number
# print("Total: " +str(total))

# import time

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# import random

# for i in range(20):
#     random_num = random.randint(0, 99999999999999999999999999)
#     print(random_num)

# a = 1
# b = 2

# if a == b:
#     print("Equal")
# else:
#     print("Not equal")

# import random

# random_num = random.randint(1, 10)
# guess = int(input("Guess the random number: "))

# if guess == random_num:
#     print("CORRECT!!!")
# else:
#     print("WRONG!!!")


# import random

# random_num1 = random.randint(1, 50)
# random_num2 = random.randint(1, 50)
# answer = random_num1 + random_num2

# user_answer = int(input("what is " + str(random_num1) + " + " + str(random_num2) + "?\n"))

# if user_answer == answer:
#     print("U GOT IT CORRECT YAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
# else:
#     print("U GOT IT WRONG!")

# import random

# num_questions = int(input("HOW MANY QUESTION DO U WANT"))
# for i in range(num_questions):
#     random_num1 = random.randint(1, 30)
#     random_num2 = random.randint(1, 30)
#     answer = random_num1 * random_num2

#    user_answer = int(input("what is" + ))

# number = int(input("PUT IN A NUMBER OR SAY BYE BYE:)"))

# if number % 2 ==0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

number1 = int(input("enter number 1: "))
number2 = int(input("enter number 2: "))

if number2 % number1 ==0:
    print("true")
else:
    print("False")
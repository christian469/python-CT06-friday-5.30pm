# # recap 1
# toppings = [
#     "mushroom",
#     "pepperoni",
#     "pineapple",
#     "onions",
#     "sausage",
#     "bacon",
#     "extra cheese",
#     "black olives",
#     "green pepers",
#     "fresh garlic",
# ]

# print("avilable toppings")
# for count in range(len(toppings)):
#     print(count+1, ":", toppings[count])

# selection = []
# question = "pls choice ur toppings by number"
# reply = input(question)
# while reply != "end":
#     index = int(reply)
#     selection.append( toppings[index-1] )
#     reply = input(question)

# print ("you have selected:")
# for one in selection:
#     print(one)
#############################################################################################
# fruits = ["apple(:", "mango):", "orangeXD", "coconut|:"]
# prices = [4, 5, 6, 7]
# for index in range(len(fruits)):
#     print(f"{fruits[index]}'s prices is {prices[index]}.")
##############################################################
# items = ["apple", "milk", "bread", "egg", "chocolate"]
# stocks = [15, 0, 8, 25, 3]
# for index in range(len(items)):
#     qty = stocks[index]
#     if qty == 0:
#         print( f"{ items[index] }: out of stock" )
#     elif qty < 10:
#         print( f"{ items[index] }: low stock" )
#     elif qty >= 10:
#         print( f"{ items[index] }: well stocked")

# # task 2b
# reply = input("what are u looking for? ")
# if reply in items:
#     found_index = items.index(reply)
#     qty = stocks[found_index]
#     print(f"we have {qty} remaining. ")
# else:
#     print("item not found in da database")
###########################################################

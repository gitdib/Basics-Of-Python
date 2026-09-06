n = int(input("How many items did you buy? "))

total = 0

for i in range(n): #The relation between the number of items and the total bill amount is that the total bill amount is calculated by adding the price of each item entered by the user. The number of items (n) determines how many times the loop will run, and for each iteration, the user is prompted to enter the price of an item. The total bill amount is then calculated by summing up all the prices entered by the user.
    price = float(input("Enter item price: "))
    total = total + price

print("The total bill amount is:", total)
print("The average bill amount is:", total / n)
#here we are calculating the total bill amount by adding the price of each item entered by the user. We then calculate the average bill amount by dividing the total by the number of items (n).
#we have taken both number and price of items purchased as input from the user. The total bill amount is calculated by adding the price of each item entered by the user. The average bill amount is calculated by dividing the total by the number of items (n).

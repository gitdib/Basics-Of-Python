a = int(input("Enter a: "))
b = int(input("Enter b: "))


for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
       print(i)
       break  #this will stop the loop after the first number is found
       

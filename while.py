# DS T07 Compulsory Task 3 - Beginner Control Structures — While Loop

# A program that calculate the average of the numbers entered.

sum = 0
count = 0

num = float(input("Enter a number (-1 to exit): ")) # Asks the user to enter a number.

while num != -1:
    sum += num
    count += 1
    num = float(input("Enter a number (-1 to exit): "))   # Always asks the user to enter a number until the user enters -1.
    if num == -1:
        avg = sum / count 
        print(f"The average of the {count} numbers entered is {avg : .2f}")
        break
    

        



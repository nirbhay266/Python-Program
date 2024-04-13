"""(61) Write a program to print all the Numbers from 1 to 100 but skip the 
 numbers from 51 to 75 using Continue statement. """
for num in range(1, 101):
    if num >= 51 and num <= 75:
        continue
    print(num)
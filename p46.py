"""(46) Write a program to enter Metro City Name and its Fahrenheit Temp. 
Then convert Fahrenheit to Celsius Temp. Then check if Celsius """

name=input("Enter Metrocity Name: ")
ft=float(input("Enter Fahrenheit Temperature"))
ct=(ft+32)*9/5

if(ct>=0):
    print("\n%s's Temperature in Celsius is %.2f" % (name, ct))
else:
    print("\nTemperature cannot be negative")
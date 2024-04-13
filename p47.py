"""(47) Write a program to enter Metro City Name and its Fahrenheit Temp. 
Then convert Fahrenheit to Celsius Temp. Then check if Celsius 
temp. Is less than 5 then print Metro City Name and Cool Day, if 
Celsius temp. is greater than and equal to 5 and less than 15 then 
print Metro City Name and Normal Day and if Celsius Temp. is 
greater than and equal to 15 then print Metro City Name and Hot Day."""

name=input("Metro City Name")
ft=input("Fahrenheit Tempreture")
ct=(float(ft)-32)*5/9
if ct<5:
    print("\n Metrocity Name:  %s \n Temperature: %.2f"% (name,ct))
    print ("Cool Day")
elif ct>=5 and ct<15:
    print("\n Metrocity Name:  %s \n Temperature: %.2f"% (name,ct))
    print ("Normal Day")
elif ct>=15:
    print("\nMetrocity Name:  %s \nTemperature: %.2f"% (name,ct))
    print ("Hot Day")
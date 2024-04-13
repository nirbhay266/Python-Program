"""(36) Write a program to enter any Number then check inputted Number is 
Even Number, if inputted No. is Even then print “Inputted Number is 
 Even Number”. """

n=int(input("Enter Number"))
if(int(n%2==0)) :
    print("Enven number",+n)
else:
    print("Not Even Number",+n)
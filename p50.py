"""(50) Write a program to enter any Alphabate Character then check inputted 
 Character is Vowel or Consonant, if input any Number or any Special 
 Character then print a message "Not a Alphabate Character"."""

n=input("Enter any Alphabate Character: ")
if(n.isalpha()):
    print("Inputted Character is Vowel or Consonant")
else:
    print("Not a Alphabate Character")
    #Wrong program
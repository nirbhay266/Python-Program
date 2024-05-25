#Sequence data type
#(1).str data type
str1='nirbhay Kumar'
sr2="Nitya Yadav"
str3='''Yadav'''
print(str1)
print(sr2)
print(str3)
print(str1[0],str1[1],str1[5])
#(2).List Data Type
list=[10,20,3.5,23,45,"Nirbhay Yadav","Stya Yadav"]
list[2]=1000
list[3]="Nitya Ray"
print(list)
#tuple Data Type
tpl=(10,20,3.5,23,45,"Nirbhay Yadav","Stya Yadav")
print(tpl)



#Sets Data Type
#(1).set Data Type
s={10,40,50,56,78,90,775,43,53}
k=set("MATH")
print(s)
print(k)
#(2)Frozenset Data Type
p=["Classic","Computer","Insitute"]
fn=frozenset(p)
print(p)
print(fn)


name=input("Enter Your Name")
age=input("Enter Your Age")

print("Your Name Is"+name)
print("Your"+age)

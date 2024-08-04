f=open("demo.txt","w")
f.write("I want to learn Python ")
f=open("demo.txt","r")
data=f.read()
print(data)

f=open("demo.txt","a")
f.write("Then move Java javascript")
f.close()

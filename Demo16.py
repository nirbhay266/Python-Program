f=open("demo.txt","r")
data1=f.readlines()
data=f.read()
print(data)
print(data1)
print(type(data))
f.close()
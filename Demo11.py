cities=["Motihari","Delti","Patna","Pune","Kolcata"]
heroes=["Tiger","Ajay","Salmam","Sahrukh"]
def print_len(list):
    print(len(list))
print_len(heroes)

def print_list(list):
    for i in list:
        print(i,end=" ")

print_list(heroes)
print_list(cities)
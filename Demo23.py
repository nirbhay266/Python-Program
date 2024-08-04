with open("Practice.txt","r") as f:
    data=f.read()

    new_data=data.replace("Python","Java")
    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)
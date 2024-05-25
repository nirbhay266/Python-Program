def converter(usd):
    inr_val=usd*83
    print(usd,"USD=",inr_val,"INR")

usd=float(input("Enter the amount in USD:"))

converter(usd)
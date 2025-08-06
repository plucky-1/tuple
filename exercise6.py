atm = 1000
accountbalance = 10000
amount = float(input("Enter the amount\n>>>>"))
if amount > 0 and amount <= accountbalance:
    print("welcome")
    if amount % atm == 0:
        accountbalance -= amount
        print("you have been paid")
    else:
        print("Invalid amount")
elif amount < accountbalance:
    print("insuficient funs")	
else:
    print("amount out of range")
print(f"your balance is:,{accountbalance}")    



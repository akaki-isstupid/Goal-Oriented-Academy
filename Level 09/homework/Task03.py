savings = input("Input savings:")

savings = float(savings)

balance = savings * 1.05
balancestring = str(balance)
message = "Amount in 1 year:" + balancestring
print(message)
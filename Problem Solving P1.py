# 1
amount = int(input("Enter the amount: "))
price = 1
wrappers_needed = 3

chocolates = amount // price
wrappers = chocolates

while wrappers >= wrappers_needed:
    new_chocolates = wrappers // wrappers_needed
    chocolates += new_chocolates
    wrappers = (wrappers % wrappers_needed) + new_chocolates

print("Total chocolates eaten:", chocolates)

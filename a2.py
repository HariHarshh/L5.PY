actual_cost = float(input(" Please Enter the Actual Product Price : "))
sale_amount = float(input(" Please Enter the Sale amount : "))
if (sale_amount > actual_cost):
     p = sale_amount - actual_cost
     print("Total Profit = {0}".format(p))
elif(actual_cost > sale_amount):
     l= actual_cost - sale_amount
     print("Total loss = {0}".format(l))
else:
     print("No Profit ... No Loss !!! ")
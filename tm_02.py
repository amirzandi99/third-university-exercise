def myHouse(x, y, z):
    tax = (z * x) * 5
    cost = x + (y * 5) * tax
    return cost
# 
hp = float(input("input house price : "))
fc = float(input("input fuel cost   : "))
tr = float(input("input tax rate    : "))
result = myHouse(hp,fc,tr)
print(f"cost : {result}")
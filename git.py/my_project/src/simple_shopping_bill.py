def calculate_total(price, quantity):
    return price * quantity


item1 = "chicken rice"
price1 = 110
quantity1 = 3

item2 = "chilly chicken"
price2 = 120
quantity2 = 6

total1 = calculate_total(price1, quantity1)
total2 = calculate_total(price2, quantity2)

grand_total = total1 + total2

print("Shopping Bill")
print(item1, ":", total1)
print(item2, ":", total2)
print("Grand Total:", grand_total)
weight = float(input("Weight: "))
print("Premium costs 125.00")
shipping = input("Which shipping would you like? (ground. ground premium, drone) ")
flat_charge = 20.00

if shipping == "ground premium":
    flat_charge = 125.00
    print(flat_charge)

#Ground Shipping
if shipping == "ground":
    if weight <= 2:
        print(weight * 1.50 + flat_charge)
    elif 2 <= weight <= 6:
        print(weight * 3.00 + flat_charge)
    elif 2 <= weight <= 10:
        print(weight * 4.00 + flat_charge)
    else:
        print(weight * 4.75 + flat_charge)

#Drone shipping
if shipping == "drone":
    if weight <= 2:
        print(weight * 4.50)
    elif 2 <= weight <= 6:
        print(weight * 9.00)
    elif 2 <= weight <= 10:
        print(weight * 12.00)
    else:
        print(weight * 14.25)
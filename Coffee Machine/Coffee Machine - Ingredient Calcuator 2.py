print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

# Read in the number of coffee drinks as input
num_coffees = int(input("Write how many cups of coffee you will need: "))

# Calculate the amount of each ingredient needed
water_needed = num_coffees * 200
milk_needed = num_coffees * 50
coffee_needed = num_coffees * 15

# Print out the required ingredient amounts
print("For " + str(num_coffees) + " cups of coffee you will need:")
print(water_needed, "ml of water")
print(milk_needed, "ml of milk")
print(coffee_needed, "g of coffee beans")
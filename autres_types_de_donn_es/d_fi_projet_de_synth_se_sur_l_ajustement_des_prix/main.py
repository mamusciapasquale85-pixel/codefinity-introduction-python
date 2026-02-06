grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15)
}

# Réduire le prix des œufs si besoin
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    old_category, old_price, old_stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (old_category, old_price - 1, old_stock)

# Ajouter Tomatoes
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

# Réapprovisionner le lait si besoin
milk_category, milk_price, milk_stock = grocery_inventory["Milk"]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (milk_category, milk_price, milk_stock + 20)

# Affichage final
print("Updated inventory:", grocery_inventory)
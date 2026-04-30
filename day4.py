"""The Challenge: The Inventory Restocker
Goal: Write a function update_inventory(current_stock, incoming_shipment, max_capacity) that updates a warehouse's stock levels.

Constraints:

Merge Stocks: Add the quantities from incoming_shipment to current_stock.

The "Max Cap" Rule: If adding an item exceeds the max_capacity for that specific item, you must cap it at that maximum and return a list of "Overflow" items (the amount that couldn't be stored).

New Items: If an item in the shipment isn't in the current stock, add it (still respecting the capacity).

Data Integrity: If a shipment quantity is negative, ignore that specific item (don't subtract from stock)."""

#Inventory Management" system.

def update_inventory(current_stock, incoming_shipment, max_capacity):
    overflow = {}

    for item, quantity in incoming_shipment.items():
        # Ignore invalid negative shipments
        if quantity <= 0:
            continue
            
        # Calculate how much we currently have (default to 0 if new)
        current_amount = current_stock.get(item, 0)
        
        # Calculate potential new total
        potential_total = current_amount + quantity
        
        if potential_total > max_capacity:
            # Set to max and calculate the leftover
            current_stock[item] = max_capacity
            overflow[item] = potential_total - max_capacity
        else:
            # Update normally
            current_stock[item] = potential_total
            
    return current_stock, overflow

# --- Test Case ---
initial_stock = {"apples": 50, "bananas": 20}
shipment = {"apples": 60, "bananas": 10, "oranges": 110, "pears": -5}
limit = 100

new_stock, leftover = update_inventory(initial_stock, shipment, limit)

print(f"Updated Stock: {new_stock}")
print(f"Overflow: {leftover}")
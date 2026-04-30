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
# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders):
    if not orders: #Check if orders list is empty
        return 0.0 # If List is Empty return 0.0
    total = 0.0
    valid_count = 0  # Changed: count only non-cancelled orders
    for order in orders:
        if order.get("status") != "cancelled": #check if order is non-canceled and use get method to skip safely if keys are missing
            amount = order.get("amount")
            if isinstance(amount,(int,float)):
                total += amount
                valid_count += 1 # count  orders
    """check if all lons are canceled and 
       Return 0.0 if all loans are canceled otherwise return average value
       """
    return total / valid_count if valid_count >0 else 0.0
# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    """Calculate the average of valid numeric measurements, ignoring None and non-convertible values."""
    if not values:
        return 0.0

    total = 0.0
    valid_count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                valid_count += 1
            except (ValueError, TypeError):
                continue  # Skip non-numeric values (strings, lists, etc.)
    return total / valid_count if valid_count > 0 else 0.0
# Prompt for input exactly as specified
kw_hours = int(input("Enter the KW hours used: "))

# Calculate the cents
if kw_hours <= 1000:
    total_cents = kw_hours * 7.633
else:
    total_cents = (1000 * 7.633) + ((kw_hours - 1000) * 9.259)

# Convert to dollars
total_dollars = total_cents / 100

# Standard print matching the first case
print(f"Amount owed is ${total_dollars}")

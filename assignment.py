# Aggregate Functions and Operators

# Find the total quantity sold using SUM
total_quantity = sum([2,5,3,1,4])
print("Total Quantity:", total_quantity)

# Find the average quantity sold
average_quantity = total_quantity / 5
print("Average Quantity:", average_quantity)

# Find the minimum price
prices = [50000,20000,30000,50000,20000]
print("Minimum Price:", min(prices))

# Find the maximum quantity
quantities = [2,5,3,1,4]
print("Maximum Quantity:", max(quantities))

# Count the number of sales records
print("Sales Records Count:", len(quantities))

# Find the total sales amount
totals = [
    2*50000,
    5*20000,
    3*30000,
    1*50000,
    4*20000
]

print("Total Sales Amount:", sum(totals))

# Find average sales amount per transaction
print("Average Sales Amount:", sum(totals)/len(totals))

# Difference between maximum and minimum price
print("Price Difference:", max(prices)-min(prices))

# Average price per item
print("Average Price Per Item:", sum(totals)/sum(quantities))

# Multiply maximum quantity with minimum price
print("Max Quantity * Min Price:", max(quantities)*min(prices))

# Total column
print("Total Column:", totals)

# Total of Total column
print("Total of Total Column:", sum(totals))

# Average of Total column
print("Average of Total Column:", sum(totals)/len(totals))

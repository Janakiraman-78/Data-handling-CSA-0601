import matplotlib.pyplot as plt

# Product Categories
categories = [
    "Groceries",
    "Dairy",
    "Fruits",
    "Vegetables",
    "Bakery",
    "Beverages",
    "Snacks",
    "Personal Care",
    "Household Items",
    "Frozen Foods"
]

# Sales (Lakhs)
sales = [120, 95, 80, 75, 68, 90, 110, 55, 70, 60]

# Create Bar Chart
plt.figure(figsize=(10,5))
plt.bar(categories, sales, color="skyblue")

# Chart Title
plt.title("Monthly Sales Revenue - June 2026")

# X and Y Labels
plt.xlabel("Product Categories")
plt.ylabel("Sales (Lakhs)")

# Rotate Category Names
plt.xticks(rotation=45)

# Save the Chart
plt.savefig("bar_chart.png")

# Show the Chart
plt.show()
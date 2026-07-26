import matplotlib.pyplot as plt

# Advertising Cost (Lakhs)
advertising_cost = [5, 8, 10, 12, 15, 18, 20, 22, 25, 28]

# Sales Revenue (Lakhs)
sales_revenue = [42, 55, 63, 70, 82, 91, 98, 110, 120, 132]

# Create Scatter Plot
plt.figure(figsize=(8,5))

plt.scatter(
    advertising_cost,
    sales_revenue,
    color="red",
    s=80
)

# Chart Title
plt.title("Advertising Cost vs Sales Revenue")

# Axis Labels
plt.xlabel("Advertising Cost (Lakhs)")
plt.ylabel("Sales Revenue (Lakhs)")

# Add Grid
plt.grid(True)

# Save Chart
plt.savefig("scatter_plot.png")

# Display Chart
plt.show()
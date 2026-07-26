import matplotlib.pyplot as plt

# Months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Energy Generated (MWh)
energy = [420, 450, 490, 530, 560, 600, 580, 590, 610, 630, 590, 540]

# Create Line Chart
plt.figure(figsize=(10,5))

plt.plot(
    months,
    energy,
    marker="o",
    color="blue",
    linewidth=2
)

# Chart Title
plt.title("Monthly Electricity Generation - 2025")

# Axis Labels
plt.xlabel("Months")
plt.ylabel("Energy Generated (MWh)")

# Rotate Month Names
plt.xticks(rotation=45)

# Add Grid
plt.grid(True)

# Save Chart
plt.savefig("line_chart.png")

# Display Chart
plt.show()
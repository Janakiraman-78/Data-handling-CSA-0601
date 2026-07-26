import matplotlib.pyplot as plt

# Marketing Channels
channels = [
    "Social Media",
    "Television",
    "Print Media",
    "Radio",
    "Email Marketing",
    "Influencer Marketing",
    "SEO",
    "Events"
]

# Budget Allocation (%)
budget = [28, 22, 10, 8, 12, 9, 6, 5]

# Create Pie Chart
plt.figure(figsize=(8,8))

plt.pie(
    budget,
    labels=channels,
    autopct="%1.1f%%",
    startangle=90
)

# Chart Title
plt.title("Marketing Budget Allocation")

# Save Chart
plt.savefig("pie_chart.png")

# Display Chart
plt.show()
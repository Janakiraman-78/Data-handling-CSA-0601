import matplotlib.pyplot as plt

# Salary Packages (LPA)
salary_packages = [3.2, 4.5, 5.0, 6.8, 7.2, 8.5, 4.8, 5.5, 6.0, 7.8, 9.2, 10.5]

# Create Histogram
plt.figure(figsize=(8,5))
plt.hist(salary_packages, bins=5, color="lightgreen", edgecolor="black")

# Chart Title
plt.title("Distribution of Salary Packages")

# Axis Labels
plt.xlabel("Salary Package (LPA)")
plt.ylabel("Number of Students")

# Save Chart
plt.savefig("histogram.png")

# Display Chart
plt.show()
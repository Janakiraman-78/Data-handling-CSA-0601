import matplotlib.pyplot as plt
import scipy.stats as stats

# Monthly Income Data (in dollars)
income = [
    2500, 2800, 3000, 3200, 3400,
    3600, 3800, 4000, 4200, 4500,
    4700, 5000, 5200, 5500, 6000
]

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(8,6))

plt.hist(income,
         bins=6,
         color="skyblue",
         edgecolor="black")

plt.title("Monthly Income Distribution - Histogram")
plt.xlabel("Income")
plt.ylabel("Frequency")

plt.savefig("../Output Images/income_histogram.png")
plt.close()

# -----------------------------
# Q-Q Plot
# -----------------------------
plt.figure(figsize=(8,6))

stats.probplot(income, dist="norm", plot=plt)

plt.title("Q-Q Plot of Monthly Income")

plt.savefig("../Output Images/income_qqplot.png")
plt.show()

print("Histogram and Q-Q Plot created successfully!")
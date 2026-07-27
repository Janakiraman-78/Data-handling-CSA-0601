import matplotlib.pyplot as plt
import numpy as np

# Daily Step Counts
steps = [3000, 4200, 5000, 6200, 7000, 8200, 9100, 10000, 11500, 13000]

# Sort the data
x = np.sort(steps)
y = np.arange(1, len(x) + 1) / len(x)

# ECDF Plot
plt.figure(figsize=(8,6))

plt.step(x, y, where='post', color='green')
plt.scatter(x, y, color='red')

plt.title("ECDF of Daily Step Counts")
plt.xlabel("Steps")
plt.ylabel("Cumulative Probability")
plt.grid(True)

plt.savefig("../Output Images/ecdf_daily_steps.png")
plt.show()
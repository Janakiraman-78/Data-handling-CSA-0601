import matplotlib.pyplot as plt
import numpy as np

# Student Marks
marks = [45, 52, 58, 60, 65, 68, 72, 75, 80, 90]

# Sort the data
x = np.sort(marks)
y = np.arange(1, len(x) + 1) / len(x)

# ECDF Plot
plt.figure(figsize=(8,6))
plt.step(x, y, where='post', color='blue')
plt.scatter(x, y, color='red')

plt.title("ECDF of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Cumulative Probability")
plt.grid(True)

plt.savefig("../Output Images/ecdf_marks.png")
plt.show()
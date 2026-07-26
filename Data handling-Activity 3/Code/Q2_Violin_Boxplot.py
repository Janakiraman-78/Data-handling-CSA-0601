import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Employee Salary Data (LPA)
data = {
    "HR": [4.2, 4.5, 4.7, 4.1, 4.6, 4.3, 4.8, 4.4, 4.9, 4.5],
    "IT": [6.5, 7.0, 7.4, 6.8, 8.2, 7.6, 8.5, 7.1, 8.8, 7.3],
    "Finance": [5.8, 6.2, 6.0, 5.9, 6.7, 6.4, 6.9, 6.1, 7.2, 6.3],
    "Marketing": [5.1, 5.3, 5.5, 5.4, 5.8, 5.6, 5.9, 5.2, 6.0, 5.4]
}

df = pd.DataFrame(data)

# Violin Plot
plt.figure(figsize=(8,6))
sns.violinplot(data=df)

plt.title("Employee Salary Analysis - Violin Plot")
plt.ylabel("Salary (LPA)")

plt.savefig("../Output images/violin_plot.png")

plt.close()

# Box Plot
plt.figure(figsize=(8,6))
sns.boxplot(data=df)

plt.title("Employee Salary Analysis - Box Plot")
plt.ylabel("Salary (LPA)")

plt.savefig("../Output images/box_plot.png")

plt.close()
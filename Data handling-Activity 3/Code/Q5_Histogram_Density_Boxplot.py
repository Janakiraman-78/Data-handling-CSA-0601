import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Daily Steps Data
data = {
    "20-30": [9500,10200,9800,11000,10500,9700,10100,10800,11200,9900],
    "31-45": [8200,8600,8400,9000,8900,8500,8700,9100,9200,8600],
    "46-60": [6500,6700,6900,7200,7000,6800,7100,7300,7400,6950]
}

df = pd.DataFrame(data)

# -------------------------
# Histogram
# -------------------------
plt.figure(figsize=(8,6))

plt.hist(df["20-30"], bins=5, alpha=0.6, label="20-30")
plt.hist(df["31-45"], bins=5, alpha=0.6, label="31-45")
plt.hist(df["46-60"], bins=5, alpha=0.6, label="46-60")

plt.title("Daily Steps - Histogram")
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("../Output images/steps_histogram.png")
plt.close()

# -------------------------
# Density Plot
# -------------------------
plt.figure(figsize=(8,6))

sns.kdeplot(df["20-30"], label="20-30", fill=True)
sns.kdeplot(df["31-45"], label="31-45", fill=True)
sns.kdeplot(df["46-60"], label="46-60", fill=True)

plt.title("Daily Steps - Density Plot")
plt.xlabel("Steps")
plt.ylabel("Density")
plt.legend()

plt.savefig("../Output images/steps_density.png")
plt.close()

# -------------------------
# Box Plot
# -------------------------
plt.figure(figsize=(8,6))

sns.boxplot(data=df)

plt.title("Daily Steps - Box Plot")
plt.ylabel("Steps")

plt.savefig("../Output images/steps_boxplot.png")
plt.close()

print("Histogram, Density Plot and Box Plot created successfully!")
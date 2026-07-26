import matplotlib.pyplot as plt
import seaborn as sns

# Website Response Time (ms)
response_time = [
    210, 225, 230, 240, 250,
    260, 270, 280, 285, 290,
    300, 305, 310, 315, 320,
    330, 340, 350, 360, 380
]

# Histogram
plt.figure(figsize=(8,6))
plt.hist(response_time,
         bins=8,
         color="skyblue",
         edgecolor="black")

plt.title("Website Response Time - Histogram")
plt.xlabel("Response Time (ms)")
plt.ylabel("Frequency")

plt.savefig("../Output images/histogram.png")
plt.close()

# Density Plot
plt.figure(figsize=(8,6))
sns.kdeplot(response_time,
            fill=True,
            color="green")

plt.title("Website Response Time - Density Plot")
plt.xlabel("Response Time (ms)")
plt.ylabel("Density")

plt.savefig("../Output images/density_plot.png")
plt.close()

print("Histogram and Density Plot created successfully!")
import matplotlib.pyplot as plt
import seaborn as sns

# Website Response Times (milliseconds)
response_times = [
    210, 220, 230, 240, 250,
    260, 270, 280, 290, 300,
    310, 320, 330, 340, 350,
    360, 370, 380, 300, 310
]

# Histogram
plt.figure(figsize=(8,6))

plt.hist(response_times, bins=8,
         color="skyblue",
         edgecolor="black")

plt.title("Website Response Time - Histogram")
plt.xlabel("Response Time (ms)")
plt.ylabel("Frequency")

plt.savefig("../Output Images/histogram.png")
plt.close()

# Density Plot
plt.figure(figsize=(8,6))

sns.kdeplot(response_times,
            fill=True,
            color="green")

plt.title("Website Response Time - Density Plot")
plt.xlabel("Response Time (ms)")
plt.ylabel("Density")

plt.savefig("../Output Images/density_plot.png")
plt.close()

print("Histogram and Density Plot created successfully!")
import matplotlib.pyplot as plt
import scipy.stats as stats

# Customer Waiting Times (minutes)
waiting_time = [
    5, 7, 8, 10, 12,
    13, 15, 17, 18, 20,
    22, 23, 25, 27, 30
]

plt.figure(figsize=(8,6))

stats.probplot(waiting_time, dist="norm", plot=plt)

plt.title("Q-Q Plot of Customer Waiting Time")

plt.savefig("../Output Images/qqplot_waiting_time.png")
plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Student Marks Data
data = {
    "Mathematics": [92, 76, 81, 65, 90, 58, 84, 71, 95, 79],
    "Physics": [88, 72, 78, 70, 94, 62, 86, 75, 91, 81],
    "Chemistry": [84, 69, 83, 68, 91, 60, 82, 73, 93, 77],
    "Programming": [95, 80, 85, 72, 96, 65, 88, 77, 98, 83],
    "English": [81, 74, 79, 75, 89, 70, 80, 72, 94, 78]
}

students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]

df = pd.DataFrame(data, index=students)

plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap="YlGnBu", linewidths=0.5)

plt.title("Student Performance Heatmap")
plt.xlabel("Subjects")
plt.ylabel("Students")

plt.savefig("../Output images/heatmap.png")

plt.show()
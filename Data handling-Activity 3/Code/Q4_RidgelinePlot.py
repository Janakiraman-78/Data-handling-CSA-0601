import pandas as pd
import matplotlib.pyplot as plt

# Electricity Consumption Data
data = {
    "Jan": [220,240,230,215,225,245,235,228,238,232],
    "Feb": [235,245,238,228,240,250,242,236,246,239],
    "Mar": [250,260,255,248,258,265,259,252,262,256],
    "Apr": [275,285,280,270,282,290,284,278,287,281],
    "May": [295,305,300,292,298,310,302,297,307,301]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,6))

offset = 0

for month in df.columns:
    values = sorted(df[month])

    plt.plot(values, [offset]*len(values), marker='o', label=month)

    offset += 1

plt.title("Ridgeline Style Plot - Electricity Consumption")
plt.xlabel("Electricity Consumption")
plt.yticks(range(len(df.columns)), df.columns)

plt.savefig("../Output images/ridgeline_plot.png")

plt.show()
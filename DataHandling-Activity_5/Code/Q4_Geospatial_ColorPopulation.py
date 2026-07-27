import matplotlib.pyplot as plt

# City Data
cities = [
    "Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi",
    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Kochi"
]

latitude = [13.08, 12.97, 17.38, 19.07, 28.61,
            18.52, 22.57, 23.02, 26.91, 9.93]

longitude = [80.27, 77.59, 78.48, 72.87, 77.21,
             73.85, 88.36, 72.57, 75.79, 76.26]

population = [11, 13, 10, 20, 32, 7, 15, 8, 4, 2]

plt.figure(figsize=(9,6))

# Scatter plot with colors based on population
scatter = plt.scatter(
    longitude,
    latitude,
    c=population,
    cmap="viridis",
    s=150,
    edgecolors="black"
)

# Add city names
for i in range(len(cities)):
    plt.text(
        longitude[i] + 0.2,
        latitude[i] + 0.2,
        cities[i],
        fontsize=9
    )

plt.title("Geospatial Map - Population Based Colors")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Color scale
cbar = plt.colorbar(scatter)
cbar.set_label("Population (Millions)")

plt.grid(True)

plt.savefig("../Output Images/population_color_map.png")

plt.show()
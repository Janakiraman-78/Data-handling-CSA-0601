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

plt.figure(figsize=(9,6))

# Plot city locations
plt.scatter(longitude, latitude, color="blue", s=80)

# Add city labels
for i in range(len(cities)):
    plt.text(longitude[i] + 0.2,
             latitude[i] + 0.2,
             cities[i],
             fontsize=9)

plt.title("Geospatial Map with City Labels")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)

plt.savefig("../Output Images/city_labels_map.png")
plt.show()
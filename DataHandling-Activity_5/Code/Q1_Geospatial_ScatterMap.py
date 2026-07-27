import matplotlib.pyplot as plt

# Dataset
cities = [
    "Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi",
    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Kochi"
]

latitude = [13.08, 12.97, 17.38, 19.07, 28.61,
            18.52, 22.57, 23.02, 26.91, 9.93]

longitude = [80.27, 77.59, 78.48, 72.87, 77.21,
             73.85, 88.36, 72.57, 75.79, 76.26]

plt.figure(figsize=(8,6))

plt.scatter(longitude, latitude,
            color="blue",
            s=80)

plt.title("Scatter Map of Indian Cities")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)

plt.savefig("../Output Images/scatter_map.png")
plt.show()
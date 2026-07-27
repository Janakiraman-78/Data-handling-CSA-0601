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

# Find highest population city
max_population = max(population)
index = population.index(max_population)

plt.figure(figsize=(9,6))

# Plot all cities
plt.scatter(longitude, latitude,
            s=100,
            color="skyblue",
            edgecolors="black")

# Highlight highest population city
plt.scatter(longitude[index], latitude[index],
            s=250,
            color="red",
            edgecolors="black",
            label="Highest Population")

# Label all cities
for i in range(len(cities)):
    plt.text(longitude[i] + 0.2,
             latitude[i] + 0.2,
             cities[i],
             fontsize=9)

plt.title("Highest Population City")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.legend()

plt.savefig("../Output Images/highest_population_city.png")
plt.show()

print("City with Highest Population :", cities[index])
print("Population :", max_population, "Million")
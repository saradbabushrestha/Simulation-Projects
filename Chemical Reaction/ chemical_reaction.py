import math
import matplotlib.pyplot as plt

# Constants
k1 = 0.008
k2 = 0.002

def chem1(c1, c2, c3, t):
    return c1 + (k2 * c3 - k1 * c1 * c2) * t

def chem2(c1, c2, c3, t):
    return c2 + (k2 * c3 - k1 * c1 * c2) * t

def chem3(c1, c2, c3, t):
    return c3 + (2 * k1 * c1 * c2 - 2 * k2 * c3) * t

# Initial concentrations
c1, c2, c3 = 25, 50, 0

time_points = []
c1_points = []
c2_points = []
c3_points = []

t = 0
while t < 10:
    temp_c1 = chem1(c1, c2, c3, 0.25)
    temp_c2 = chem2(c1, c2, c3, 0.25)
    temp_c3 = chem3(c1, c2, c3, 0.25)

    time_points.append(t)
    c1_points.append(temp_c1)
    c2_points.append(temp_c2)
    c3_points.append(temp_c3)

    c1, c2, c3 = temp_c1, temp_c2, temp_c3
    t += 0.25

# Plotting the results
plt.figure(figsize=(12, 8))

# Plot for c1
plt.plot(time_points, c1_points, label="c1", color="blue")

# Plot for c2
plt.plot(time_points, c2_points, label="c2", color="red")

# Plot for c3
plt.plot(time_points, c3_points, label="c3", color="green")

plt.xlabel("Time (t)")
plt.ylabel("Concentration")
plt.title("Chemical Concentrations Over Time")
plt.legend()
plt.grid()
plt.show()

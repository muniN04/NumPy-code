import numpy as np 
import matplotlib.pyplot as plt

#parameters
balls= 50
p=0.3
matches = 1000

# Simulate matches 
results = np.random.binomial(
    n=balls,
    p=p,
    size=matches
)

#average
average=np.mean(results)

#histogram
plt.figure(figsize=(12,6))

plt.hist(
    results,
    bins=15,
    edgecolor="black"
    )

#mean line 
plt.axvline(
    average,
    color="green",
    linestyle='dashed',
    linewidth=2
    )

plt.title("Cricket Boundary Simulation")
plt.xlabel("Number of bounderies")
plt.ylabel("Number of Matches")
plt.show()

print("Average Boundaries : ", average)


import numpy as np
import matplotlib.pyplot as plt

#uniform distribution 

#number of simulation 
num_rolls=10000


# simulation part of dies
diesc_round=np.random.randint(1,7, size=num_rolls) 

counts=np.bincount(diesc_round)[1:] #couts of each occurence

probabilities = counts / num_rolls # probability of each occurence dies

# -----------------------------
# PRINT RESULTS
# -----------------------------

print("Dice Value   Frequency   Probability")

for i in range(6):
    print(
        f"{i+1:^10}"
        f"{counts[i]:^10}"
        f"{probabilities[i]:.4f}"
    )

#histogram

plt.figure(figsize=(15,10))
plt.bar(
    np.arange(1,7),
    probabilities,
    edgecolor="black"
    )

plt.axhline(
    y=1/6,
    linestyle="--",
    color="red",
    linewidth=4,
    label="Theoretical Probability"
    )

plt.title("Uniform Distribution of Fair Dice")
plt.xlabel(" dies numbers")
plt.ylabel("dies occures of probabilities")
plt.legend()

plt.show()
import numpy as np 
import matplotlib.pyplot as plt

r_point=50000 #random point

x=np.random.uniform(-1,1,r_point)
y=np.random.uniform(-1,1,r_point)

inside=(x**2 + y**2) <= 1

plt.figure(figsize=(19,10))

#inside circle 
plt.scatter(
    x[inside],
    y[inside],
    s=5,
    alpha=0.5,
    label="inside circle"
    )

#outside circle
plt.scatter(
    x[~inside],
    y[~inside],
    s=6,
    alpha=0.7,
    label="Outside circle"
    )

plt.title("Monte Carlo Pi Estimation")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.legend()
plt.show()

pi_estimate = 4 * np.sum(inside) / r_point
print("Estimated Pi:", pi_estimate)
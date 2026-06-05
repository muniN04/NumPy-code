import numpy as np 
import matplotlib.pyplot as plt 

#parameters
coins=2
p=0.5
expiriment_rounds=1000

# simulate random events 
result=np.random.normal(
    loc=coins,
    scale=p,
    size=expiriment_rounds
    )

#Statistic Mesurment
mean=np.mean(result)
varience=np.var(result)
std=np.std(result)

#report of coind simulation with mesurments 
print(f"Mean : {mean:.2f} \nVarience : {varience:.2f} \nStandard Diviation : {std:.2f}")

# Histogram
plt.figure(figsize=(20,10))
plt.hist(
    result,
    bins=2,
    edgecolor="black"
)

plt.axvline(
    mean,
    color="red",
    linestyle="dashed",
    linewidth=2
)

plt.title("coins simulation ")
plt.ylabel("Number of expriments")
plt.xlabel("Number of coins toss")
plt.show()



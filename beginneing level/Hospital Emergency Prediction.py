import numpy as np
import matplotlib.pyplot as plt 

# arrivals dynamic pattern
arrivals_patterns=[
    2,2,3,3,4,5,
    6,7,8,9,10,9,
    8,7,6,5,6,8,
    10,11,9,7,5,3
    ]

# hours generate 
hours=np.arange(1,25)

# simulation of patient arrival
arrival_simulation=np.random.poisson(
    lam=arrivals_patterns
    )

#over and busy time 
busy_threshold=8
overload_threshold=10

busy_hours=np.where(
    arrival_simulation >= busy_threshold
    )[0]+1

overload_hours=np.where(
    arrival_simulation >= overload_threshold
    )[0]+1

# reports
print("arrival simulation : ",arrival_simulation)
print("Arrivals       : ",arrival_simulation)
print("Busy Hours     : ",busy_hours)
print("Overload Hours : ",overload_hours)

#plots (visuvalization)
plt.figure(figsize=(15,9))

plt.plot(hours,
         arrival_simulation,
         marker='o',
         markerfacecolor='red',
         markeredgecolor='yellow',
         linestyle='--',
         linewidth=3,
         color='blue',
         markersize=12)

plt.axhline(y=overload_threshold,
            color='orange',
            linewidth=4,
            label='overload threshold')

# busy hours
for hour in busy_hours:
    plt.axvline(x=hour,
                color='green',
                linewidth=2)
    
# overload hours
for hour in overload_hours:
    plt.axvline(x=hour,
                color='orange',
                linewidth=2)

plt.axhline(y=busy_threshold,
            color='green',
            linewidth=4,
            label="busy hour")



plt.title("patient emergency arrival simulation")
plt.ylabel("no of arrivals")
plt.xlabel(" hours")
plt.xticks(hours)
plt.grid()
plt.legend()
plt.show()


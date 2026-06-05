import numpy as np
import matplotlib.pyplot as plt

# parameters
averge_call=23

# simulation 24 hourse

call_simulation=np.random.poisson(
    lam = averge_call,
    size = 24
    )

#hours
hours=np.arange(1,25)

# hourly traffic 
for h ,c in zip(hours , call_simulation):
    print(f"Hours : {h} calls : {c}")

# peak traffic
peack_call = np.max(call_simulation)
peak_hour = np.argmax(call_simulation)+1

print("\n peack Traffic")
print(f"peack call : {peack_call}")
print(f"peak hours : {peak_hour}")

# detect the overload
overload_threasold = 30
overload_hour = np.where(call_simulation > overload_threasold)[0]+1

print("\noverload hours :", overload_hour)

# visuvalization

plt.figure(figsize=(15,9))
plt.plot(hours,
         call_simulation,
         marker='o',
         markerfacecolor="red",
         markeredgecolor='green',
         color='red',
         linestyle='--',
         linewidth=2,
         markersize=8,
         label="calls")

plt.axhline(y=overload_threasold,
            color='blue',
            linestyle=':',
            label='overload limit')

plt.xlabel("hours")
plt.ylabel("calls per hours")
plt.title("call center simulation")
plt.legend()
plt.xticks(hours)
plt.grid()
plt.show()




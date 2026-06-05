import numpy as np
import matplotlib.pyplot as plt

# Parameters 
user_entr = 1000

# possible probability 
A_campain_p = 0.05
B_campain_p = 0.08

# generate simulation 
A_campain_simulater = np.random.binomial(
    n = 1,
    p = A_campain_p,
    size = user_entr
    )

B_campain_simulater = np.random.binomial( 
    n = 1,
    p = B_campain_p,
    size = user_entr
    )

# total CLicks 
A_clicks_total = np.sum(A_campain_simulater)
B_clicks_total = np.sum(B_campain_simulater)

# CRT click trough rate 
A_crt = A_clicks_total/user_entr
B_crt = B_clicks_total/user_entr

# EXpect Measurment values (Mean , std , zscore )

A_mean = user_entr * A_campain_p # mean
A_std =  np.sqrt(
    user_entr * A_campain_p * ( 1 - A_campain_p ) # standerd diviation
    )

#Z score 

A_Z_score = (A_clicks_total - A_mean)/A_std

# print result 
print("==================================================================")
print(f"A campain clicks   : {A_clicks_total}")
print(f"B campain clicks   : {B_clicks_total}")

print(f"A campain CRT      : {A_crt}")
print(f"B campain CRT      : {B_crt}")

print(f"Expect Values      : {A_mean}")
print(f"Standerd diviation : {A_std}")
print(f"Z score            : {A_Z_score}")
print("==================================================================")

# vizuvalizaion 

plt.figure(figsize=(14,10))

# chart 1 - bart chart for total clicks 

plt.subplot(2,2,1)

campains=["campains A","campains B"]
totalclicks=[A_clicks_total, B_clicks_total]

plt.bar(campains,totalclicks)
plt.title("Total cliscks between compain A and B")
plt.ylabel("number of clicks")

#chart 2 - crt with bar chart 

plt.subplot(2,2,2)

total_crt=[A_crt*100,B_crt*100]
plt.bar(campains,total_crt)
plt.title("CRT comparison ")
plt.ylabel("CRT (%)")

# chart 3 - histogram user clicks distribution

plt.subplot(2,2,3)

plt.hist(
    A_campain_simulater,
    bins=np.arange(-0.5,2,1),
    edgecolor="black"
    )

plt.xticks([0,1],["No clicks","clicks"])
plt.title("user click distribution")
plt.ylabel("number of clciks")

# chart 4 - outlier 
plt.subplot(2,2,4)

x = np.arange(1,101)
y = (
    1 / (A_std * np.sqrt(2 * np.pi))
    ) * np.exp(-0.5 * ((x-A_mean)/A_std) ** 2)

plt.plot(x,y)

plt.axvline(A_clicks_total,linestyle='--')

plt.title("outlier")
plt.xlabel("Clicks")
plt.ylabel("Probability density")

#layout
plt.tight_layout()

# show 
plt.show()
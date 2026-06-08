import numpy as np 
import matplotlib.pyplot as plt 

#number of student
no_student=100

# generate random study hours
Study_hours = np.random.uniform( 0 , 10 ,no_student )

logits = (Study_hours -5) # set mid point to prectics the pass result 


pass_probability=(
    1/(1 + np.exp(-logits))
    )

# pass and fail outcome
result = np.random.binomial (1 , pass_probability)

#logistic curve 

x = np.linspace(0 , 10 ,500)

y = (1/(1 + np.exp(-(x-5))))

plt.figure(figsize=(19,10))

plt.scatter(
    Study_hours,
    result,
    alpha=0.5,
    label="student"
    )

plt.plot(
    x,
    y,
    linewidth=3,
    label="logistic curve"
    )

plt.xlabel("Student hours")
plt.ylabel("pass probability")
plt.title("pass and fail probability")

plt.legend()
plt.grid(True)

plt.show()

# new student 

new_student = 7

prediction = (
    1 / (1 + np.exp(-(new_student - 5)))
)

print(
    f"Pass probability: {prediction:.2f}"
)


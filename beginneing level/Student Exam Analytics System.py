import numpy as np
import matplotlib.pyplot as plt

#generate marks 
np.random.seed(42)

marks=np.random.normal(loc=65,scale=15,size=10000) #students marks 

#limited marks
marks=np.clip(marks,0,100)
marks=marks.astype(int)

#statistics 
print("Average : ", np.mean(marks))
print("Highest : ", np.max(marks))
print("Lowest  : ", np.min(marks))
print("STD     : ", np.std(marks))

#topper student 
topper=marks[marks>=90]
print("Topper students : " , len(topper))

#fail student 
fail_student=marks[marks<45]
print("Fail Students : ",len(fail_student))

#grade 
grade=[]

for mark in marks:
    if mark >=90:
        grade.append("A")
    elif mark >=75:
        grade.append("B")
    elif mark >=60:
        grade.append("C")
    elif mark >=45:
        grade.append("D")
    else:
        grade.append("F")

#Grade Counts
unique,count =np.unique(grade,return_counts=True)
print("\nGrade Distribution")

for g,c in zip(unique,count):
    print(g," : ",c)

#outlier Detection 
mean=np.mean(marks)
std=np.std(marks)

z_score=(marks-mean)/std

outlier=marks[np.abs(z_score)>3]

print("\n Outlier    : ", outlier)
print("Total Outlier : ",len(outlier))

#Graph
plt.hist(marks,bins=30)
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()
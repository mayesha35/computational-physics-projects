

# eular method for nuclear decay

import matplotlib.pyplot as plt
lamda = float(input("enter the constant value:"))
x0 = float(input("enter the initial value of x:"))
y0 = float(input("enter the initial value of y:"))
h = float(input("enter the value of h:"))

# solve for a single value
x = float(input("enter the final value of x:"))
n = round((x - x0)/h)
e = y0
for loop in range(1,n+1):
    f = e + h*(lamda*e)
    e = f
print(e)

# for graph plot
x_list = []
for g in range(1,50):
    a1 = x0 + 0.1 * g
    x_list.append(a1)

y_list = [] # this is for eular solve data
for l in range(0,len(x_list)):
    n = round((x_list[l] - x0)/h)
    e = y0
    for loop in range(1,n+1):
        f = e + h*(lamda*e)
        e = f
    y_list.append(e)
main_y_list=[] # this list is for the solved equation data
for i in range(len(x_list)):
    N = y0*2.71828182845904523536028747135266249775724709369995**(lamda*x_list[i])
    main_y_list.append(N)

# graph plot
plt.plot(x_list,y_list, label="Eular")
plt.plot(x_list,main_y_list, label = "analytical")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.title("Growth graph")
plt.show()

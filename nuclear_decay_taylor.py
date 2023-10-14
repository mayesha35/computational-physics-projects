 import matplotlib.pyplot as plt
def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x-1)
print("please enter the initial and the finding value of t in the range of [0,1), because we only can calculate with this method only when the value of x is in between [0,1) ")    
t0 = float(input("initial value of time (t0) : "))
N0 = float(input("initial value of atoms (N0) : "))
const = float(input("constant value lambda : "))
t = float(input("final value of (t) : "))
no_of_term = int(input("how many terms do you want to count : "))
y0 = N0
for n in range(1,no_of_term+1):
    N = y0 + ((-1)**n)* N0*const*((t-t0)**n)/fact(n)
    y0 = N
print(f"at time {t} no of atoms are {y0}")
x_list = []
y_list = []
for i in range(99):
    x = t0 + 0.01*i
    x_list.append(x)
    z0 = N0
    for j in range(1,no_of_term+1):
        N1 = z0 + ((-1)**j)*N0*const*((x-t0)**j)/fact(j)
        z0 = N1
    y_list.append(z0)
main_y_list=[] # this list is for the solved equation data
for i in range(len(x_list)):
    N2 = N0*2.71828182845904523536028747135266249775724709369995**(-const*x_list[i])
    main_y_list.append(N2)

plt.plot(x_list,y_list, label = "Taylor")
plt.plot(x_list,main_y_list, label ="Analytical")
plt.legend()
plt.show()

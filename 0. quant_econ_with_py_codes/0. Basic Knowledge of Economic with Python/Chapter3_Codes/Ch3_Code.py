import numpy as np 
import matplotlib.pyplot as plt

def func_one():
    x = np.random.randn(100)
    plt.plot(x)
    plt.show()

def func_two():
    ts_length=100
    c_values=[]
    for i in range(ts_length):
        e=np.random.randn()
        c_values.append(e)
    plt.plot(c_values)
    plt.show()

def func_three():
    ts_length=100
    c_values=[]
    j = 0
    while j < ts_length:
        e = np.random.randn()
        c_values.append(e)
        j = j + 1
    plt.plot(c_values)
    plt.show()

def generate_data(n,generator_type):
    c_values=[]
    for i in range(n):
        if generator_type=="U":
            e= np.random.uniform(0,1)
        else:
            e=np.random.randn()
        c_values.append(e)
    return c_values

a = input("Which one function would you choose?")
print("You choose function:" + a)
if a == "1":
    func_one()
elif a == "2":
    func_two()
elif a == "3":
    func_three()
elif a == "4":
    b = input("Would you want to choose Uniform(0,1)?[y/n]")
    if b == "y":
        data = generate_data(100,"U")
        plt.plot(data)
        plt.show()
    elif b == "n":
        data = generate_data(100,"N")
        plt.plot(data)
        plt.show()
    else: 
        print("WTF you want to plot?")
else:
    def generate_date(n,typer):
        c_values = [typer() for i in range(n)]
    data = generate_data(100,np.random.uniform)
    plt.plot(data)
    plt.show()


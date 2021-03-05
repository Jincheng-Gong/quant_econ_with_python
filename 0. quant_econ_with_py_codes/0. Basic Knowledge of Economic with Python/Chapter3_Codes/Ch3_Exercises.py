def exercise1():
    def factorial(n):
        if n == 0:
            return 0
        elif n > 0:
            sum = 1
            while n > 1:
                sum = sum * n
                n = n - 1
            return sum
        else:
            return "Please input a POSITIVE integer number!"
    try:
        n = int(input("Please input a positive integer number:"))
        print(factorial(n))
    except:
        print("Please input a POSITIVE INTEGER NUMBER!")

def exercise2():
    from numpy.random import uniform
    def binomial_rv(n,p):
        count = 0
        for i in range(n):
            U = uniform()
            if U < p:
                count = count + 1
        return count
    return print(binomial_rv(100,0.2))

def exercise3():
    import numpy as np
    n = 1000000
    count = 0
    for i in range(n):
        x, y = np.random.uniform(), np.random.uniform()
        d = np.sqrt(x*x+y*y)
        if d < 1:
            count = count + 1
    area = count/n
    print(area*4)

def exercise4():
    from numpy.random import uniform
    n = 10
    count = 0
    for i in range(n):
        e = uniform()
        if e > 0.5:
            count = count + 1
    if count >= 5:
        print("You got one dollar.")
    else:
        print("You got nothing.")

def exercise5():
    import numpy as np
    import matplotlib.pyplot as plt
    final_value = [0]
    for i in range(201):
        final_value.append(0.9 * final_value[i] + np.random.randn())
        i = i + 1
    plt.plot(final_value)
    plt.show()

def exercise6():
    import numpy as np
    import matplotlib.pyplot as plt
    alpha_group = [0, 0.8, 0.98]
    for alpha in alpha_group:
        final_value = [0]
        for i in range(201):
            final_value.append(alpha * final_value[i] + np.random.randn())
            i = i + 1
        plt.plot(final_value, label = "Alpha = " + str(alpha))
    plt.legend()
    plt.show()

#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
exercise6()
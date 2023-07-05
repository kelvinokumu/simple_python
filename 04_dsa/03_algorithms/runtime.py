# proposed complexities
constant_complexity = "O(1)"
linear_complexity = "O(N)"
quadratic_complexity = "O(N^2)"
cubic_complexity = "O(N^3)"


# functions
def function1(N):
    for i in range(N):
        print(i)


def function2(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                print(i, j, k)


def function3(N):
    for i in range(10000):
        print(i)


def function4(N):
    for i in range(N):
        for j in range(N):
            for k in range(10):
                print(i, j, k)


def function5(N):
    for i in range(N):
        for j in range(10000):
            print(i, j)


# Add your answers below
answer1 = linear_complexity
answer2 = cubic_complexity
answer3 = constant_complexity
answer4 = quadratic_complexity
answer5 = linear_complexity
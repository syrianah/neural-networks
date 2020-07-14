# Gradient descent
import random


def check_epsilon(x_new, x_old, epsilon):
    sum = 0.0
    for i in range(len(x_new)):
        sum += abs(x_new[i] - x_old[i])
    if sum < epsilon:
        return False
    return True


def first_function(x_1, x_2):
    return 2*x_1**2 + x_2**2 - 2 * x_1 * x_2 - 2 * x_1 + 1


def calculate_first_gradient(x_old, epsilon, c):
    print("First gradient")
    print(f"Values: [{x_old[0], x_old[1]}]")
    # function we are calculating gradient for
    print("f(x_1, x_2) = 2x_1^2 + x_2^2 - 2x_1 * x_2 - 2x_1 + 1")
    x_new = list(x_old)  # copy x_old to x_new
    flag = True
    while(flag):
        # assign x_old elements to variables for brevity
        x = x_old[0]
        y = x_old[1]
        x_new[0] = x - c * (4 * x - 2 * y - 2)
        x_new[1] = y - c * (2 * y - 2 * x)
        flag = check_epsilon(x_new, x_old, epsilon)
        x_old = list(x_new)  # copy x_new to x_old
    print(f"Point({x_new[0]}, {x_new[1]})")
    print(f"Value: {first_function(x_new[0], x_new[1])}\n")


def second_function(x_1, x_2):
    # x ** y => x to the power of y
    return x_1**4/2 - x_1**3/3 - x_1**2/2 + x_2**2 - 2*x_2 + 1


def calculate_second_gradient(x_old, epsilon, c):
    print("Second gradient")
    print(f"Values: [{x_old[0], x_old[1]}]")
    print("f(x_1, x_2) = x_1^4/2 - x_1^3/3 - x_1^2/2 + x_2^2 - 2x_2 + 1\n")
    flag = True
    while(flag):
        # assign x_old elements to variables for brevity
        x = x_old[0]
        y = x_old[1]
        x_new = list(x_old)  # copy x_old to x_new
        x_new[0] = x - c * (2 * x ** 3 - x ** 2 - x)
        x_new[1] = y - c * (2 * y - 4)
        flag = check_epsilon(x_new, x_old, epsilon)
        x_old = list(x_new)  # copy x_new to x_old
    print(f"Point({x_new[0]}, {x_new[1]})")
    print(f"Value: {second_function(x_new[0], x_new[1])}\n")


def main():
    print("Gradient descent\n")
    # Predefine epsilon and c constant
    epsilon = 0.00001
    c = 0.01
    # Generate list of length 2 with random floats between -5 <= x < 5
    input_first = [round(random.uniform(-2, 2), 2) for i in range(2)]
    calculate_first_gradient(input_first, epsilon, c)
    # Generate list of length 2 with random floats between -3 <= x < 3
    input_second = [round(random.uniform(-2, 2), 2) for i in range(2)]
    calculate_second_gradient(input_second, epsilon, c)


if __name__ == "__main__":
    main()

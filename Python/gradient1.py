import random

# Predefine epsilon and c constant
epsilon = 0.00001
c = 0.01


def check_epsilon(x_new, x_old):
    '''
    Check if summed difference between x_new and x_old is grater than epsilon.
    Retrun true if yes, else return false.
    '''
    sum = 0.0
    for i in range(len(x_new)):
        sum += abs(x_new[i] - x_old[i])
    if sum < epsilon:
        return False
    return True


class f1:
    '''Class representing first function'''

    def print_f(self):
        return f"f(x1, x2) = 2x1^2 + x2^2 - 2x1x2 - 2x1 + 1 \n"

    def prime_x1(self, x1, x2):
        return x1 - c * (4 * x1 - 2 * x2 - 2)

    def prime_x2(self, x1, x2):
        return x2 - c * (2 * x2 - 2 * x1)

    def value(self, x1, x2):
        return (2 * x1 ** 2) + (x2 ** 2) - (2 * x1 * x2) - (2 * x1) + 1


class f2:
    '''Class representing second function'''

    def print_f(self):
        return f"f(x1, x2) = x1^4/2 - x1^3/3 - x1^2/2 + x2^2 - 2x2 + 1\n"

    def prime_x1(self, x1, x2):
        return x1 - c * (2 * x1 ** 3 - x1 ** 2 - x1)

    def prime_x2(self, x1, x2):
        return x2 - c * (2 * x2 - 4)

    def value(self, x1, x2):
        return (x1 ** 4)/2 - (x1 ** 3)/3 - (x1 ** 2)/2 + (x2 ** 2) - (2 * x2) + 1


def calculate_gradient(x_old, function):
    print("Gradient for: " + function.print_f())
    print(f"Values: [{x_old[0], x_old[1]}]")

    x_new = list(x_old)  # copy x_old to x_new
    flag = True

    while(flag):

        x1 = x_old[0]
        x2 = x_old[1]

        x_new[0] = function.prime_x1(x1, x2)
        x_new[1] = function.prime_x2(x1, x2)

        flag = check_epsilon(x_new, x_old)

        x_old = list(x_new)  # copy x_new to x_old

    print(f"Point({x_new[0]}, {x_new[1]})")
    print(f"Value: {function.value(x_new[0], x_new[1])}\n")


def main():
    # Generate list of length 3 with random floats between -5 <= x < 5
    # input_first = [round(random.uniform(-5, 5), 2) for i in range(2)]
    input_first = [4.99093, 2.0636]
    calculate_gradient(input_first, f1())

    # Generate list of length 2 with random floats between -3 <= x < 3
    # input_second = [round(random.uniform(-3, 3), 2) for i in range(2)]
    input_second = [-0.185367, 0.246715]
    calculate_gradient(input_second, f2())


if __name__ == "__main__":
    main()

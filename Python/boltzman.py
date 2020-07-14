# Python
import random

euler = 2.718281828459


def main():
    temperatures = [0.01, 0.1, 1, 3, 10]

    z_list = [1 if x < 10 else 0 for x in range(20)]

    vec_c = get_c_vector(z_list)
    vec_w = get_w_vector(vec_c)
    theta = get_theta(vec_c)

    for temperature in temperatures:

        print("Current temperature: {}".format(temperature))
        x = [[] for _ in range(11)]
        x[0] = gen_random_vector()
        t = 0

        while(t < 10):

            beta = gen_beta_vector()
            for i in range(20):

                if(beta[i] >= 0 and beta[i] <= f_uit(vec_w[i], x[t], theta[i], temperature)):
                    x[t+1].append(1)
                elif(beta[i] <= 1 and beta[i] >= f_uit(vec_w[i], x[t], theta[i], temperature)):
                    x[t+1].append(0)

            t += 1
            print_vector(x[t])


def f_uit(w, x, theta, temperature):

    s = 0
    uit = 0
    for j in range(20):
        s += w[j]*x[j]
        uit = s - theta

    return 1 / (1 + euler ** (-(uit/temperature)))


def get_theta(vec):
    ''' Return theta value for vector'''
    sum = [0]*20
    for i in range(20):
        for j in range(20):
            sum[i] += vec[i][j]
    return sum


def get_w_vector(vec):
    ''' Compute vector "w" from vector "c"'''
    w = [[] for _ in range(len(vec))]
    for i in range(20):
        for j in range(20):
            w[i].append(2*vec[i][j])
    return w


def get_c_vector(vec):
    '''Generate "c" vector from "z" list '''
    c = [[] for _ in range(len(vec))]
    for i in range(len(vec)):
        for j in range(len(vec)):
            if i != j:
                c[i].append((vec[i] - 0.5) * (vec[j] - 0.5))
            else:
                c[i].append(0.0)
    return c


def gen_random_vector():
    '''Generate random list, each element is 0 or 1.'''
    return [random.randint(0, 1) for x in range(20)]


def gen_beta_vector():
    '''Generate random list, each element is range from 0 to 1.'''
    return [random.random() for x in range(20)]


def print_vector(vec):
    for i in range(len(vec)):
        if (vec[i] <= 0.0):
            print(" _ ", end='')
        else:
            print(" * ", end='')
    print(" ")


if __name__ == "__main__":
    main()

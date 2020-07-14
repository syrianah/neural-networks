# Boltzmann Machine

from math import e
from math import log
import random
import time as systime

def main():
    temperature = 5.0
    time = 5.0

    x_list = [
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0
    ]
    
    vec_c = get_vector_c(x_list)
    vec_x = gen_random_vec()
    print_vector(vec_x)
    
    while(time < 51): # while(True)
        vec_x = gen_next_vec(vec_x, vec_c)
        time += 1.0
        systime.sleep(1)
        print("Time: " + str(time) + " - temperature: " + str(temperature))
        print_vector(vec_x)

def get_theta(vec):
    sum = 0.0
    for i in range(25):
        sum += vec[i]
    return sum
 
def get_vector_c(vec):
    out = [[]*25] * 25
    tmp = []
    for i in range(25):
        tmp.clear()
        for j in range(25):
            if i != j:
                tmp.append((vec[i] -0.5) * (vec[j] - 0.5))
            else:
                tmp.append(0.0)
        out[i] = tmp[:]
    return out
 
def gen_random_vec():
    vec = [
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
    ]
    temp = []
    for i in range(25):
        if (vec[i] % 2 == 0):
            temp.append(1.0)
        else:
            temp.append(0.0)
 
    return temp
 
 
def gen_next_vec(prev, vecC):
    vec = []
    uit = 0.0
    for i in range(25):
        uit = 0.0
        for j in range(25):
            uit += 2 * vecC[i][j] * prev[j]
        uit-= get_theta(vecC[i])
        if uit > 0:
            vec.append(1.0)
        elif uit == 0:
            vec.append(prev[i])
        else:
            vec.append(0.0)
    return vec
 
def print_vector(vec):
    line = ""
    for i in range(25):
        if (vec[i] <= 0.0):
            line += "   "
        else:
            line += " * "
 
        if (i % 5 == 4):
            print(line)
            line = ""

if __name__ == "__main__":
    main()
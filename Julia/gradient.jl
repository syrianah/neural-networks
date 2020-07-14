using Distributions

function check_epsilon(x_new, x_old, epsilon)
    sum = 0.0
    for i in 1:length(x_new)
        sum += abs(x_new[i] - x_old[i])
    end
    if sum < epsilon
        return false
    end

end

function first_f(x1, x2)
    return 2x1^2 + x2^2 - 2x1 * x2 - 2x1 + 1
end

function calculate_first_gradient(x_old, epsilon, c)
    println("First gradient")
    println(string("Values: " , x_old))
    println("f(x1, x2) = 2x1^2 + x2^2 - 2x1 * x2 - 2x1 + 1")
    x_new = copy(x_old)
    flag = true
    while(flag)
        x1 = x_old[1]
        x2 = x_old[2]
        x_new[1] = x1 - c * (4x1 - 2x2 - 2)
        x_new[2] = x2 - c * (2x2 - 2x1)
        flag = check_epsilon(x_new, x_old, epsilon)
        x_old = x_new
    end
    println(string("Point ", x_new))
    # println()
    println(string("Value: ", first_f(x_new[1], x_new[2])))
end

function second_f(x1, x2)
    # x ** y => x to the power of y
    return x1^4/2 - x1^3/3 - x1^2/2 + x2^2 - 2*x2 + 1
end

function calculate_second_gradient(x_old, epsilon, c)
    println("Second gradient")
    println(string("Values: " , x_old))
    println("f(x1, x2) = x1^4/2 - x1^3/3 - x1^2/2 + x2^2 - 2x2 + 1")
    x_new = zeros(2)
    flag = true
    while(flag)
        x1 = x_old[1]
        x2 = x_old[2]
        x_new = x_old
        x_new[1] = x1 - c * (2 * x1^3 - x1^2 - x1)
        x_new[2] = x2 - c * (2x2 - 4)
        flag = check_epsilon(x_new, x_old, epsilon)
        x_old = x_new
    end
    println(string("Point ", x_new))
    # println()
    println(string("Value: ", second_f(x_new[1], x_new[2])))
end

function main()
    print("Gradient descent\n")
    # Predefine epsilon and c constant
    epsilon = 0.00001
    c = 0.01
    # Generate list of length 3 with random floats between -5 <= x < 5
    # input_first = [rand(Uniform(-5, 5)) for x in 1:2]
    input_first = [4.99093, 2.0636]
    # input_first = [10, 2]
    calculate_first_gradient(input_first, epsilon, c)
    # input_second = [rand(Uniform(-2, 2)) for x in 1:2]
    input_second = [-0.185367, 0.246715]
    calculate_second_gradient(input_second, epsilon, c)
    # println(input_first[1])
    # println(rand(Uniform(-2, 2)))
end

main()
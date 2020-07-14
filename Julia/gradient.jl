function check_epsilon(x_new, x_old, epsilon)
    sum = 0.0
    for i in 0:length(x_new)
        sum += abs(x_new[i] - x_old[i])
    end
    if sum < epsilon
        return false
    end

end

function first(x_1, x_2)
    return 2x_1^2 + x_2^2 - 2x_1 * x_2 - 2x_1 + 1
end

function calculate_first_gradient(x_old, epsilon, c)
    println("First gradient")
    println(x_old)
    println("f(x_1, x_2) = 2x_1^2 + x_2^2 - 2x_1 * x_2 - 2x_1 + 1")

end

function main()
    print("Gradient descent\n")
    # Predefine epsilon and c constant
    epsilon = 0.00001
    c = 0.01
    # Generate list of length 3 with random floats between -5 <= x < 5


end
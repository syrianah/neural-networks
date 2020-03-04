# Perceptron

function dot(v1, v2, m)
    x = 0
    for i in 1:m
        x += v1[i] * v2[i]
    end
    return x
end

function f(weights, inputs, m)
    if dot(weights, inputs, m) >= 0
        return 1
    else return 0
    end
end

function z(t)
    if (mod(t, 5) + 1) <= 3
        return 1.0
    else 
        return 0.0
    end
end

function iter(c, inputs)
    weights = ones(26)
    t = 1
    counter = 0.0

    while counter < 5.0
        zt = z(t)
        yt = f(inputs[mod(t, 5) + 1], weights, length(weights))
        for i in 1:26
            weights[i] = weights[i] + c * (zt - yt) * inputs[mod(t, 5) + 1][i]
        end
        t += 1
        if zt == yt
            counter += 1.0
        else
            counter = 0.0
        end
    end
    println(string("C: ", c, "\tT: ", t))
    for i in 1:length(weights)
        println(string("W", i, ": ", weights[i]))
    end
end

function main()
    inputs = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0]]

    for c in [0.01, 0.1, 1.0]
        iter(c, inputs)
    end
end

main()

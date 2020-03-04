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
    if (t % 5 + 1) <= 3
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
        yt = f(inputs[t % 5], weights, length(weights))
        for i in 1:26
            weights[i] = weights[i] + c * (zt - yt) * inputs[t % 5][i]
        end
        t += 1
        if zt == yt
            counter += 1.0
        else
            counter = 0.0
        end
    end
    print(string(c, t))
end

iter(1, 1)
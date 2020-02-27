using LinearAlgebra


weights = [0.3, 0.3, -0.5]
inputs = [1, 1, 1]

x = 0
for i in 1:3
    global x += weights[i] * inputs[i]
end

# println(weights[1])
println(x)

println(dot(weights, inputs))
# Ćwiczenia 1
# Model McCulloch-Pittsa

# Zad: Kożystając z modelu neurony M.-Pittsa, zaimplementować następujące
# bramki logiczne (znaleźć w_i(i <= i <= n)).
# 1) NOT
# 2) AND
# 3) NAND
# 4) OR

using LinearAlgebra

function f(weights, inputs)
    if dot(weights, inputs) >= 0
        return 1
    else return 0
    end
end

function not_gate()
    weights = [-0.5, 0.3]
    print("\033[92mNOT GATE \nInput: \033[0m")
    x = parse(Int64, readline())
    if isa(x, Number)
        inputs = [x, 1]
    else
        print("\nBad input")
        return
    end
    println(string("Result: ", f(weights, inputs)))
end

function and_gate()
    weights = [0.3, 0.3, -0.5]
    print("\033[92mAND GATE \nInput 1: \033[0m")
    x = parse(Int64, readline())
    print("\033[92mInput 2: ")
    y = parse(Int64, readline())
    if isa(x, Number)
        inputs = [x, y, 1]
    else
        print("\nBad input")
        return
    end
    println(string("Result: ", f(weights, inputs), "\033[0m"))
end

function nand_gate()
    weights = [-0.4, -0.4, 0.6]
    print("\033[95mNAND GATE \n\033[92mInput 1: \033[0m")
    x = parse(Int64, readline())
    print("\033[92mInput 2: ")
    y = parse(Int64, readline())
    if isa(x, Number)
        inputs = [x, y, 1]
    else
        print("\nBad input")
        return
    end
    println(string("Result: ", f(weights, inputs), "\033[0m"))
end

function or_gate()
    weights = [0.3, 0.3, -0.2]
    print("\033[95mOR GATE \n\033[92mInput 1: \033[0m")
    x = parse(Int64, readline())
    print("\033[92mInput 2: ")
    y = parse(Int64, readline())
    if isa(x, Number)
        inputs = [x, y, 1]
    else
        print("\nBad input")
        return
    end
    println(string("Result: ", f(weights, inputs), "\033[0m"))
end



# println(f(100))
# not_gate()
# and_gate()
# nand_gate()
# or_gate()
def fibon(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    result = fibonacci[-1]
    return result

print("The 5^th fibonacci element is:", fibon(6))
print("The 10^th fibonacci element is:", fibon(11))
print("The 15^th fibonacci element is:", fibon(16))
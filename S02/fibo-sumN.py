
def fibosum(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    m = 0
    for i in fibonacci[:n]:
        m += i
    return m

print("The sum of the first five elements of the fibonacci series is:", fibosum(6))
print("The sum of the first ten elements of the fibonacci series is:", fibosum(11))
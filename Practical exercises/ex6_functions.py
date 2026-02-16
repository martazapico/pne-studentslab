#6a: Basic function:
def is_even(number):
    if number % 2 == 0:
        return True
    elif number % 2 != 0:
        return False
print(f'is_even(4) = {is_even(4)}')
print(f'is_even(7) = {is_even(7)}')
print(f'is_even(0) = {is_even(0)}')
print(f'is_even(-3) = {is_even(-3)}')
print(f'is_even(10) = {is_even(10)}')

#6b: Function with multiple parameters
def classify_triangle(a, b, c):
    if a == b:
        if b == c:
            result = "equilateral"
        elif b != c:
            result = "isosceles"
    elif a == c:
        if b == c:
            result = "equilateral"
        elif b != c:
            result = "isosceles"
    elif b == c:
        if a == c:
            result = "equilateral"
        elif a != c:
            result = "isosceles"
    elif a != b != c:
        result = "scalene"
    return result

print(f'classify_triangle(5, 5, 5) = {classify_triangle(5, 5, 5)}')
print(f'classify_triangle(3, 3, 4) = {classify_triangle(3, 3, 4)}')
print(f'classify_triangle(3, 4, 5) = {classify_triangle(3, 4, 5)}')

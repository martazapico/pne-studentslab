def grade(score):
    if 0.0 <= score <= 2.9:
        result = "F"
    elif 3 <= score <= 4.9:
        result = "D"
    elif 5.0 <= score <= 6.9:
        result = "C"
    elif 7.0 <= score <= 8.9:
        result = "B"
    elif 9.0 <= score <= 10.0:
        result = "A"
    else:
        result = "Your score is invalid. Please enter a valid score"
    return result
print(f'Score {9.5} -> {grade(9.5)}')
print(f'Score {7.0} -> {grade(7.0)}')
print(f'Score {5.5} -> {grade(5.5)}')
print(f'Score {3.2} -> {grade(3.2)}')
print(f'Score {1.0} -> {grade(1.0)}')

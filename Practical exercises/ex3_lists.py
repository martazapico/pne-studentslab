temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
#The temperature on Wednesday (index 2)
def wednesday(temperatures):
    result = temperatures[2]
    return result
#The maximum temperature
def max_temp(temperatures):
    result = max(temperatures)
    return result
#The minimum temperature
def min_temp(temperatures):
    result = min(temperatures)
    return result
#The average temperature (rounded to 1 decimal)
def av_temp(temperatures):
    total = sum(temperatures)
    result = total/len(temperatures)
    result = round(result, 1)
    return result
#The number of days above 17 degrees
def above(temperatures):
    count = 0
    for i in temperatures:
        if i > 17:
            count += 1
    return count
#The list sorted from lowest to highest
def sorted(temperatures):
    temperatures.sort()
    return temperatures

print("The temperature on Wednesday is:", wednesday(temperatures))
print("The maximum temperature is:", max_temp(temperatures))
print("The minimum temperature is:", min_temp(temperatures))
print("The average temperature is:", av_temp(temperatures))
print("The number of days above 17 degrees is:", above(temperatures))
print("The list sorted from lowest to highest is:", sorted(temperatures))
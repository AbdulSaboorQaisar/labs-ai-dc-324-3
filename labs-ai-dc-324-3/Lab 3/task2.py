# Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [ Formula: c/5 = f-32/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit] 

# Expected Output: 
# 60°C is 140 in Fahrenheit 45° F is 7 in Celsius 

celsius_temp = 60
fahrenheit_temp = 45

def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius

print(F"{celsius_temp}°C is {int(celsius_to_fahrenheit(celsius_temp))} in Fahrenheit")
print(F"{fahrenheit_temp}°F is {int(fahrenheit_to_celsius(fahrenheit_temp))} in Celsius")


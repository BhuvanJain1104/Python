def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


temp=int(input("Enter Temprature:"))
degree=input("Enter [F/C]:")

if degree.upper()=="F":
        print(f"Temprature is {fahrenheit_to_celsius(temp)}°C")

elif degree.upper()=="C":
        print(f"Temprature is {celsius_to_fahrenheit(temp)}°F")
        






















     
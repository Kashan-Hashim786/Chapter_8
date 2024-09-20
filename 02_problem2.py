# °F = (9/5 × °C) + 32.


def C2F(celcius):
    return (9/5 * celcius) + 32

celcius_Temperature = float(input("Enter a temperature in celcius : "))
fahrenheit_Temperature = C2F(celcius_Temperature)
print(f"{celcius_Temperature}°C is equal to {fahrenheit_Temperature}°F")

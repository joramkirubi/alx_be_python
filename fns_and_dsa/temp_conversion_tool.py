# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    Formula: (F - 32) * 5/9
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    Formula: (C * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Ask user for temperature
    temp_input = input("Enter the temperature to convert: ")

    try:
        temperature = float(temp_input)
    except ValueError:
        # Must raise ValueError with exact message
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Ask user for unit (C or F)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid unit. Please enter C or F.")

if __name__ == "__main__":
    main()


#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary to map Roman numerals to integers
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Loop through the roman_string in reverse
    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)

        if value >= prev_value:
            total += value  # Add if the current value is greater or equal
        else:
            total -= value  # Subtract if the current value is smaller

        prev_value = value

    return total

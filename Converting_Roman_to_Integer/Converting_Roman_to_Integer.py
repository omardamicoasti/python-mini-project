import sys

# Define the dictionary mapping Roman numerals to integers
roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def convert_to_integer(roman_str):
    num = 0
    prev_value = 0

    for char in roman_str:
        if char not in roman_dict:
            print(f"Invalid character '{char}' found in the input Roman numeral.")
            return None

        curr_value = roman_dict[char]
        num += curr_value

        if curr_value > prev_value:
            # If the current value is greater than the previous value, subtract twice the previous value
            num -= 2 * prev_value

        prev_value = curr_value

    return num


def main():


    roman_str = input("Enter a Roman numeral: ").upper()
    integer_value = convert_to_integer(roman_str)

    if integer_value is not None:
        print(integer_value)


if __name__ == "__main__":
    main()

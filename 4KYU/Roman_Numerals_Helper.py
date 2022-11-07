class RomanNumerals(object):
    roman_number_dictionary = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    @staticmethod
    def to_roman(number):
        _number = number
        roman_number_dictionary = RomanNumerals.roman_number_dictionary
        roman = ''
        for key in roman_number_dictionary:
            roman_number = roman_number_dictionary[key]
            while _number >= roman_number:
                roman += key
                _number -= roman_number

        return roman

    @staticmethod
    def from_roman(line):
        _line = line
        roman_number_dictionary = RomanNumerals.roman_number_dictionary
        number = 0
        previous_character = 0

        for i in range(len(line) - 1, -1, -1):
            if roman_number_dictionary[line[i]] >= previous_character:
                number += roman_number_dictionary[line[i]]
            else:
                number -= roman_number_dictionary[line[i]]

            previous_character = roman_number_dictionary[line[i]]

        return number
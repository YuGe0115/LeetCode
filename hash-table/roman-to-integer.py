class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

        result = 0

        for i in range(len(s) - 1):
            current_value = roman_values[s[i]]
            next_value = roman_values[s[i + 1]]
            
            if current_value < next_value:
                result -= current_value

            else:
                result += current_value

        result += roman_values[s[-1]]
        
        return result
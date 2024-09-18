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

        total = 0
        length = len(s)

        for i in range(length):
            current_value = self.romanValue(s[i])
            if i < length - 1 and current_value < self.romanValue(s[i + 1]):
                total -= current_value
            else:
                total += current_value

        return total

    def romanValue(self, char: str) -> int:
        if char == 'I':
            return 1
        elif char == 'V':
            return 5
        elif char == 'X':
            return 10
        elif char == 'L':
            return 50
        elif char == 'C':
            return 100
        elif char == 'D':
            return 500
        elif char == 'M':
            return 1000
        return 0  # Invalid Input
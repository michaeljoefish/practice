class Solution:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'IV': 4,
        'IX': 9,
        'L': 50,
        'C': 100,
        'IV': 40,
        'IX': 90,
        'D': 500,
        'M': 1000,
        'IV': 400,
        'IX': 900,
    }

    def romanToInt(self, s: str) -> int:
        sum = 0

        for i in range(0, len(s)-1, 2):
            sub = s[i : i+2]

            if sub in Solution.roman_dict:
                sum += Solution.roman_dict[sub]
            else:
                sum += Solution.roman_dict[sub[0]]
                sum += Solution.roman_dict[sub[1]]
        
        if len(s)%2 == 1:
            sum += Solution.roman_dict[s[-1]]
        
        return sum
        
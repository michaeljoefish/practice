class Solution:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        sum = 0
        last = 0

        sum += Solution.roman_dict[s[0]]
        last = sum

        for i in range(1, len(s)):
            temp = Solution.roman_dict[s[i]]
            if temp > last:
                sum += temp - 2*last
                last = temp - last
            else:
                sum += temp
                last = temp
        
        return sum

bob = Solution()

print(bob.romanToInt("MCMXCIV"))
print(bob.romanToInt("LVIII"))
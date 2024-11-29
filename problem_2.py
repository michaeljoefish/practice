class Solution:
    pow_dict = {}
    def myPow(self, x: float, n: int) -> float:
        Solution.pow_dict = {}
        Solution.pow_dict[0] = 1
        Solution.pow_dict[1] = x
        result =  self.powHelper(x, abs(n))
        if n < 0:
            return 1 / result
        return result
    
    def powHelper(self, x: float, n: int) -> float:
        if n in Solution.pow_dict:
            return Solution.pow_dict[n]
        if n%2 == 0:
            Solution.pow_dict[n] = self.powHelper(x, n//2) * self.powHelper(x, n//2)
        else:
            Solution.pow_dict[n] = self.powHelper(x, n//2) * self.powHelper(x, n//2) * x
        
        return Solution.pow_dict[n]

bob = Solution()

print(bob.myPow(2.0, 10))
print(bob.myPow(2.1, 3))
print(bob.myPow(2.0, -2))
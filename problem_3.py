class Solution:
    min_dict = {}
    def coinChange(self, coins: list[int], amount: int) -> int:
        Solution.min_dict = {}
        Solution.min_dict[0] = 0

        for i in coins:
            Solution.min_dict[i] = 1
        
        return self.coinHelper(coins, amount)

    def coinHelper(self, coins: list[int], amount: int) -> int:
        if amount in Solution.min_dict:
            return Solution.min_dict[amount]
        min = 11000

        for i in coins:
            if i <= amount:
                temp = self.coinHelper(coins, amount-i)
                if temp != -1:
                    if temp < min:
                        min = 1 + temp
        
        if min < 11000:
            Solution.min_dict[amount] = min
        else:
            Solution.min_dict[amount] = -1
        
        return Solution.min_dict[amount]
                
bob = Solution()

print(bob.coinChange([1,2,5], 11))
print(bob.coinChange([2], 3))
print(bob.coinChange([1], 0))
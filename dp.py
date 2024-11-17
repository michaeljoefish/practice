class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        temp = 0

        for i in range(0,n):
            temp = two
            two = one+two
            one = temp
        
        return one
    
    res_list = [-1]
    sum = 0
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost_length = len(cost)
        Solution.res_list *= cost_length
        return min(self.minCost(cost, 0, cost_length) , self.minCost(cost, 1, cost_length))

    def minCost(self, cost: list[int], start: int, length: int):
        if length - start == 1:
            return cost[start]
        if length - start == 2:
            return min(cost[start], cost[start] + cost[start+1])
        
        return cost[start] + min(self.minCost(cost, start+1, length) , self.minCost(cost, start+2, length))

bob = Solution()

"""print(bob.climbStairs(3))
print(bob.climbStairs(4))
print(bob.climbStairs(5))"""
print(bob.minCostClimbingStairs([5,1,1,1,5,2,1,1]))
print(bob.minCostClimbingStairs([15,20]))
print(bob.minCostClimbingStairs([10,15,20]))
print(bob.minCostClimbingStairs([0,1,1,0]))
print(bob.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


    #(2)
    #1,1
    #2
    #(3)
    #1,1,1
    #1,2
    #2,1
    #(4)
    #1,1,1,1
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
            return cost[start]
        
        return cost[start] + min(self.minCost(cost, start+1, length) , self.minCost(cost, start+2, length))
    
    def test_func(self, cost):
        res = [cost[-1],cost[-2]]

        for i in range(len(cost)-3, -1, -1):
            #print(f"{i}:{sum},{left},{right},b")
            res.append(cost[i] + min(res[-1], res[-2]))
            #print(f"{i}:{left},{right},{sum}a")
        
        return min(res[-1], res[-2])
    dp_list = []
    def rob(self, nums: list[int]) -> int:
        Solution.dp_list.append(nums[-1])
        return self.rob_num(nums, 0, len(nums))

    def rob_num(self, nums: list[int], start: int, length):
        if length - start <= len(Solution.dp_list):
            return Solution.dp_list[length-start-1]
        
        Solution.dp_list.append(max(nums[start] + self.rob_num(nums, start+1, length), Solution.dp_list[length-start-1]))
        return Solution.dp_list[length-start-1]
        """if length - start == 1:
            return nums[start]
        if length - start == 2:
            return max(nums[start], nums[start+1])
        
        return max(nums[start] + self.rob_num(nums, start+2, length), self.rob_num(nums, start+1, length))"""

bob = Solution()

"""print(bob.climbStairs(3))
print(bob.climbStairs(4))
print(bob.climbStairs(5))
print(bob.minCostClimbingStairs([5,1,1,1,5,2,1,1]))
print(bob.minCostClimbingStairs([15,20]))
print(bob.minCostClimbingStairs([10,15,20]))
print(bob.minCostClimbingStairs([0,1,1,0]))
print(bob.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(bob.test_func([5,1,1,1,5,2,1,1]))
print(bob.test_func([15,20]))
print(bob.test_func([10,15,20]))
print(bob.test_func([0,1,1,0]))
print(bob.test_func([1,100,1,1,1,100,1,1,100,1]))"""
#print(bob.rob([2,1,1,2]))
#print(bob.rob([1,2,3,1]))
print(bob.rob([2,7,9,3,1]))
print(bob.rob([3]))
print(bob.rob([2,3]))


    #(2)
    #1,1
    #2
    #(3)
    #1,1,1
    #1,2
    #2,1
    #(4)
    #1,1,1,1
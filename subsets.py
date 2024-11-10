class Solution:
    res = []
    sol = []

    def subsets(self, nums: list) -> list[list]:

        return []
    
    def extract(self, nums, stay: int, next: int):
        if next+1 >= len(nums):
            self.res.append(self.sol[:])
        
        if stay >= 0:
            self.sol.append(nums[stay])
        
        self.sol.append(nums[next])
    

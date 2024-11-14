class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        slide_sum = 0
        max_sum = 0

        for i in range(k):
            slide_sum += nums[i]

        max_sum = slide_sum

        for i in range(k,len(nums)):
            slide_sum -= nums[i-k]
            slide_sum += nums[i]
            if slide_sum > max_sum: max_sum = slide_sum
        
        return max_sum/k
    
    def longestOnes(self, nums: list[int], k: int) -> int:
        p1 = 0
        p2 = 0

        max_size = 0
        zero_count = 0

        while p2 < len(nums):
            if zero_count < k:
                if nums[p2] == 0:
                    zero_count += 1
                p2 += 1
            elif zero_count == k:
                if nums[p2] != 0:
                    p2 += 1
                else:
                    zero_count += 1
                    diff = p2 - p1
                    if diff > max_size: max_size = diff
            else:
                if nums[p1] == 0:
                    zero_count -= 1
                p1 += 1
            
            diff = p2 - p1
            if diff > max_size: max_size = diff

            return max_size



def main():
    bob = Solution()

    print(bob.findMaxAverage([1,12,-5,-6,50,3], 4))
    print(bob.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))

if __name__ == "__main__":
    main()

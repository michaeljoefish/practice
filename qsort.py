class Solution:
    def sortArray(self, nums: list) -> list:
        self.qsort_ep(nums, 0, len(nums) - 1)
        return nums

    def qsort_ep(self, nums: list, start: int, piv: int):
        bp = piv
        ws = bp


        for i in range(start,piv):
            if (nums[i] < nums[piv]) and (bp < piv):
                temp = nums[i]
                nums[i] = nums[ws]
                nums[ws] = temp
                bp = i
                ws += 1
            elif (nums[i] > nums[piv]) and (bp >= piv):
                bp = i
                ws = bp

        
        
        
        temp = nums[piv]
        nums[piv] = nums[ws]
        nums[ws] = temp

        print(f"{start},{piv}")

        if (ws - start) >= 2:
            self.qsort_ep(nums, start, ws-1)
        if (piv - ws) >= 2:
            self.qsort_ep(nums, ws+1, piv)

def main():
    bob = Solution()
    print(bob.sortArray([5,2,3,1]))
    print(bob.sortArray([7,2,1,6,8,5,3,4]))


    

def is_sorted(l: list):
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return False
        
if __name__ == "__main__":
    main()
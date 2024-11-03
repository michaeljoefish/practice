class Solution:
    def sortArray(self, nums: list) -> list:
        self.qsort_ep(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums: list, start: int, piv: int):
        i = start - 1


        for j in range(start,piv):
            if nums[j] < nums[piv]:
                i += 1
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

        
        
        
        temp = nums[piv]
        nums[piv] = nums[i+1]
        nums[i+1] = temp

        return i+1
    
    def qsort_ep(self, nums, start, piv):
        if start < piv:
            #print(f"{start},{piv}: {nums}")
            p = self.partition(nums, start, piv)

            self.qsort_ep(nums, start, p-1)
            self.qsort_ep(nums, p+1, piv)

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
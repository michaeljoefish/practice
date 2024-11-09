class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        end_ind = len(numbers)-1

        i = 0

        while i < end_ind:
            
            if numbers[i] + numbers[end_ind] == target:
                return [i+1,end_ind+1]
            elif numbers[i] + numbers[end_ind] > target:
                end_ind -= 1
            else:
                i += 1
        
        return []
    

def main():
    bob = Solution()
    print(bob.twoSum([2,7,11,15], 9))
    print(bob.twoSum([2,3,4], 6))
    print(bob.twoSum([-1,0], -1))

if __name__ == "__main__":
    main()
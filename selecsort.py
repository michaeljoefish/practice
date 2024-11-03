def sel_sort(nums: list):

    for i in range(0, len(nums)):
        min = i
        for k in range(i+1, len(nums)):
            if nums[k] < nums[min]:
                min = k
        
        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp
    
    return nums

def main():
    lst = [5,3,6,2,4,1,7]
    sel_sort(lst)
    print(lst)

if __name__ == "__main__":
    main()
        
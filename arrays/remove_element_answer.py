# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val. Consider the number of elements in nums which are not equal to val be k, 
# to get accepted, you need to do the following things: Change the array nums such that the first k elements of nums contain the elements 
# which are not equal to val. The remaining elements of nums are not important as well as the size of nums. Return k.

class Solution(object):
    @staticmethod
    def removeElement(nums, val):
        k = 0 # Pointer for placing elements
        for i in range(len(nums)): # iterate through array
            if nums[i] != val: # if number doesnt equal value
                nums[k] = nums[i] # swap the number to the front
                k += 1 # increment the pointer forward
        return k # k is the index at which the numbers start equalling the val


nums = [1,2,3,3,6]
val = 3
result = Solution.removeElement(nums, val)
print(result)


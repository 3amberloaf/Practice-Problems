# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums. Consider the number of 
# unique elements of nums to be k, to get accepted, you need to do the following things: Change the array nums such that the first k elements 
# of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important 
# as well as the size of nums. Return k.

class Solution:
    @staticmethod
    def removeDuplicates(nums):
        
        k = 1  # since the first element is always unique if the list is not empty
        for i in range(1, len(nums)):  # start from the second element
            if nums[i] != nums[k-1]:  # compare with the previous element
                nums[k] = nums[i]  # move unique element to the next position for unique elements
                k += 1  # increase count of unique elements
        
        return k, nums[:k]

nums = [1, 2, 3, 3, 4, 4]
result = Solution.removeDuplicates(nums)
print(result)  # Expected output: 4
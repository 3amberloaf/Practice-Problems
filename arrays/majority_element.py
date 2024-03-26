# Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

class Solution(object):
    @staticmethod
    def majorityElement(nums):
        counts = {}
        for num in nums: # iterate through each element in the array
            if num in counts: # if the number is in the counts dictionary
                counts[num] += 1 # increment the count for that number
            else:
                counts[num] = 1 # otherwise keep it at one
            if counts[num] > len(nums) // 2:
                return num

nums = [3, 2, 3]
result = Solution.majorityElement(nums)
print(result)  

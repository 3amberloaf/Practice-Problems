# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    @staticmethod
    def rotate(nums, k):
        n = len(nums)
        k = k % n  # In case k is greater than the array length
        nums[:] = nums[-k:] + nums[:-k]

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution.rotate(nums, k)
print(nums)  # This will print the rotated array

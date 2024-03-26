#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    @staticmethod
    def merge(nums1, m, nums2, n):
        # pointers for nums1, nums2, and the end of the merged array
        i, j, k = m - 1, n - 1, m + n - 1
        
        # Merge in non descending order
        while j >= 0: # checks that there are elements in nums2 to be merged
            if i >= 0 and nums1[i] > nums2[j]: # compares nums1 to nums2
                nums1[k] = nums1[i] # move the next highest number to position k
                i -= 1 # go down the array
            else:
                nums1[k] = nums2[j] # either there arent any more numbers in nums1 or nums2 is bigger
                j -= 1 # go down nums2
            k -= 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
Solution.merge(nums1, m, nums2, n)
print(nums1) 

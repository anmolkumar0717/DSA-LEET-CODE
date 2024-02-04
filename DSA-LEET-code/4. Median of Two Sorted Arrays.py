class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        if (n%2==0):
            num3=(nums[int(n/2)]+nums[int((n/2)-1)])/2
            return num3
        else:
            return nums[n//2]

                
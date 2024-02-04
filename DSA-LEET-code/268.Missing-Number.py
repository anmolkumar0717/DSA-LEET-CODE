class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)+1
        fullsum=int(length*(length-1))/2
        missing_sum=sum(nums)
        miss=int(fullsum-missing_sum)
        return miss

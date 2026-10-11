class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        val=len(nums)
        sumy=0
        for i in range(1,val+1):
            if val%i==0:
                sumy+=nums[i-1]**2
        return sumy
                
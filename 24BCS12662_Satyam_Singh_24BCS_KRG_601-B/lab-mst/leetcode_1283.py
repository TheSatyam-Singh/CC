class Solution:
    def smallestDivisor(self, nums, threshold):
        left=1
        right=max(nums)
        while left<right:
            mid=(left + right)//2
            s=0
            for i in nums:
                s+=(i+mid-1)//mid
            if s<=threshold:
                right=mid
            else:
                left=mid + 1
        return left

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=[]
        res.append(nums[0])
        current_largest_sum=res[0]
        for n in range(1, len(nums)):
            res.append(max(res[n-1] + nums[n], nums[n]))
            if res[n]>current_largest_sum:
                current_largest_sum=res[n]
        return current_largest_sum

# Time Complexcity=O(N)
# Space Complexcity=O(N)
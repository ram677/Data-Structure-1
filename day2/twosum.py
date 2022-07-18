class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            y=target-nums[i]
            if y in d.keys():
                return[d[y],i]
            else:
                d[nums[i]]=i
        return []

#Time Complexcity=O(n)
#Space Complexcity=O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

#Time Complexcity=O(n*n)
#Space Complexcity=O(1)
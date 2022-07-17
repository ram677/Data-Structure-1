class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result=set()
        for n in nums:
            if n not in result:
                result.add(n)
            else:
                return True
        return False
    
# Time Complexcity=O(N)
# Space Complexcity=O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result=set(nums)
        if len(result)<len(nums):
            return True
        else:
            return False

# Time Complexcity=O(1)
# Space Complexcity=O(N)
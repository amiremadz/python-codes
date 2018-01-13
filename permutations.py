# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        if(len(nums) == 1):
            result.append(nums)
            return result 
            
        for i, item in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            perms = self.permute(rest)
            
            for perm in perms:
                result.append([item] + perm)
            
        return result    
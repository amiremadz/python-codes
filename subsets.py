# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution_iterative:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subs = [[]]
        
        for num in nums:
            n = len(subs)
            for idx in range(n):
                sub = copy.deepcopy(subs[idx])
                subs.append(sub)
                subs[-1].append(num)
        
        return subs

class Solution_iterative:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subs = [[]]
        
        for num in nums:
            subs += [sub + [num] for sub in subs]
        
        return subs

class Solution_bitmanip:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n_subs = 2 ** len(nums)
     
        subs = []
        subs += [[] for _ in range(n_subs)]
    
        for idx_num , num in enumerate(nums):
            for idx_sub in range(n_subs):
                if (idx_sub >> idx_num) & 1:
                    subs[idx_sub] += [num]
        
        return subs

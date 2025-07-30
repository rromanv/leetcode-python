from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Two Sum
        
        https://leetcode.com/problems/two-sum/
        
        Difficulty: Easy
        
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        
        Algorithm: Hash Map - Store each number and its index. For each number, 
                check if its complement (target - num) exists in the map.
        Time Complexity: O(n) - Single pass through array
        Space Complexity: O(n) - Hash map storage
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
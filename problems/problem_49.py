from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        49. Group Anagrams
        
        https://leetcode.com/problems/group-anagrams/
        
        Difficulty: Medium
        
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.
        
        Algorithm: Hash map with sorted word as key
        Time Complexity: O(n * k * log k) where n = number of strings, k = max string length
        Space Complexity: O(n * k) for storing all strings and hash map
        """ 
        if not strs:
            return []

        anagram_groups = {}

        for word in strs:
            sorted_key = tuple(sorted(word))

            if(sorted_key in anagram_groups) :
                anagram_groups[sorted_key].append(word)
            else:
                anagram_groups[sorted_key] = [word]
        return list(anagram_groups.values())
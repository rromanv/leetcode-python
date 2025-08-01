import pytest
import sys
import os

# Add the parent directory to the path so we can import from problems
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from problems.problem_49 import Solution


class TestGroupAnagrams:
    def test_typical_case(self):
        """Test typical case with multiple anagram groups"""
        solution = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = solution.groupAnagrams(strs)
        
        # Sort both the outer list and inner lists for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        
        assert result_sorted == expected_sorted
    
    def test_empty_list(self):
        """Test with empty input list"""
        solution = Solution()
        strs = []
        result = solution.groupAnagrams(strs)
        assert result == []
    
    def test_single_string(self):
        """Test with single string input"""
        solution = Solution()
        strs = ["hello"]
        result = solution.groupAnagrams(strs)
        assert result == [["hello"]]
    
    def test_no_anagrams(self):
        """Test with strings that have no anagrams"""
        solution = Solution()
        strs = ["abc", "def", "ghi"]
        result = solution.groupAnagrams(strs)
        
        # Sort both the outer list and inner lists for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        
        expected = [["abc"], ["def"], ["ghi"]]
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        
        assert result_sorted == expected_sorted
    
    def test_all_anagrams(self):
        """Test with all strings being anagrams of each other"""
        solution = Solution()
        strs = ["silent", "listen", "enlist"]
        result = solution.groupAnagrams(strs)
        
        # Sort the inner list for comparison
        result_sorted = [sorted(group) for group in result]
        expected = [["enlist", "listen", "silent"]]
        expected_sorted = [sorted(group) for group in expected]
        
        assert result_sorted == expected_sorted
    
    def test_duplicate_strings(self):
        """Test with duplicate strings"""
        solution = Solution()
        strs = ["eat", "eat", "tea", "ate"]
        result = solution.groupAnagrams(strs)
        
        # Sort both the outer list and inner lists for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        
        expected = [["ate", "eat", "eat", "tea"]]
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        
        assert result_sorted == expected_sorted
    
    def test_single_character_strings(self):
        """Test with single character strings"""
        solution = Solution()
        strs = ["a", "b", "c", "a"]
        result = solution.groupAnagrams(strs)
        
        # Sort both the outer list and inner lists for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        
        expected = [["a", "a"], ["b"], ["c"]]
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        
        assert result_sorted == expected_sorted
    
    def test_long_strings(self):
        """Test with longer strings"""
        solution = Solution()
        strs = ["abcdef", "fedcba", "xyz", "zyx"]
        result = solution.groupAnagrams(strs)
        
        # Sort both the outer list and inner lists for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        
        expected = [["abcdef", "fedcba"], ["xyz", "zyx"]]
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        
        assert result_sorted == expected_sorted
    
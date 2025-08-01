import pytest
import sys
import os

# Add the parent directory to the path so we can import from problems
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from problems.problem_56 import Solution


class TestMergeIntervals:
    def test_typical_case(self):
        """Test typical case with overlapping intervals"""
        solution = Solution()
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = solution.merge(intervals)
        expected = [[1, 6], [8, 10], [15, 18]]
        assert result == expected
    
    def test_all_overlapping(self):
        """Test when all intervals overlap"""
        solution = Solution()
        intervals = [[1, 4], [4, 5], [2, 6], [3, 7]]
        result = solution.merge(intervals)
        expected = [[1, 7]]
        assert result == expected
    
    def test_no_overlapping(self):
        """Test when no intervals overlap"""
        solution = Solution()
        intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]
        result = solution.merge(intervals)
        expected = [[1, 2], [3, 4], [5, 6], [7, 8]]
        assert result == expected
    
    def test_empty_list(self):
        """Test with empty input list"""
        solution = Solution()
        intervals = []
        result = solution.merge(intervals)
        assert result == []
    
    def test_single_interval(self):
        """Test with single interval"""
        solution = Solution()
        intervals = [[1, 3]]
        result = solution.merge(intervals)
        expected = [[1, 3]]
        assert result == expected
    
    def test_adjacent_intervals(self):
        """Test intervals that are adjacent (touch but don't overlap)"""
        solution = Solution()
        intervals = [[1, 2], [2, 3], [3, 4]]
        result = solution.merge(intervals)
        expected = [[1, 4]]
        assert result == expected
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        solution = Solution()
        intervals = [[-3, -1], [-2, 2], [1, 3]]
        result = solution.merge(intervals)
        expected = [[-3, 3]]
        assert result == expected
    
    def test_large_numbers(self):
        """Test with large numbers"""
        solution = Solution()
        intervals = [[1000000, 2000000], [1500000, 2500000], [3000000, 4000000]]
        result = solution.merge(intervals)
        expected = [[1000000, 2500000], [3000000, 4000000]]
        assert result == expected
    
    def test_duplicate_intervals(self):
        """Test with duplicate intervals"""
        solution = Solution()
        intervals = [[1, 3], [1, 3], [2, 6], [2, 6]]
        result = solution.merge(intervals)
        expected = [[1, 6]]
        assert result == expected
    
    def test_complex_overlapping(self):
        """Test complex overlapping scenario"""
        solution = Solution()
        intervals = [[1, 10], [2, 5], [3, 7], [4, 6], [8, 12], [9, 11]]
        result = solution.merge(intervals)
        expected = [[1, 12]]
        assert result == expected
    
    def test_zero_intervals(self):
        """Test intervals containing zero"""
        solution = Solution()
        intervals = [[0, 2], [1, 3], [-1, 1]]
        result = solution.merge(intervals)
        expected = [[-1, 3]]
        assert result == expected
    
    def test_single_point_intervals(self):
        """Test intervals that are single points"""
        solution = Solution()
        intervals = [[1, 1], [2, 2], [3, 3]]
        result = solution.merge(intervals)
        expected = [[1, 1], [2, 2], [3, 3]]
        assert result == expected
    
    def test_mixed_point_and_range_intervals(self):
        """Test mix of point intervals and range intervals"""
        solution = Solution()
        intervals = [[1, 1], [2, 4], [3, 3], [5, 5]]
        result = solution.merge(intervals)
        expected = [[1, 1], [2, 4], [5, 5]]
        assert result == expected 
import sys
import os

# Add the parent directory to the path so we can import from problems
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from problems.problem_1 import Solution


class TestTwoSum:
    """Test cases for the two_sum function."""
    
    def setup_method(self):
        """Set up the Solution instance for each test."""
        self.solution = Solution()
    
    def test_basic_example(self):
        """Test the basic example from the problem description."""
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        assert result == [0, 1] or result == [1, 0]
    
    def test_second_example(self):
        """Test the second example from the problem description."""
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        assert result == [1, 2] or result == [2, 1]
    
    def test_third_example(self):
        """Test the third example from the problem description."""
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        assert result == [0, 1] or result == [1, 0]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = self.solution.twoSum(nums, target)
        assert result == [2, 4] or result == [4, 2]
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers in the array."""
        nums = [1, 5, 3, 5, 7]
        target = 10
        result = self.solution.twoSum(nums, target)
        assert result == [1, 3] or result == [3, 1]
    
    def test_large_numbers(self):
        """Test with large numbers."""
        nums = [1000000, 2000000, 3000000, 4000000]
        target = 5000000
        result = self.solution.twoSum(nums, target)
        # Check that the result is valid (any valid pair)
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_small_array(self):
        """Test with the smallest possible array (2 elements)."""
        nums = [1, 2]
        target = 3
        result = self.solution.twoSum(nums, target)
        assert result == [0, 1] or result == [1, 0]
    
    def test_zero_target(self):
        """Test with target value of 0."""
        nums = [1, -1, 2, -2, 3]
        target = 0
        result = self.solution.twoSum(nums, target)
        assert result == [0, 1] or result == [1, 0] or result == [2, 3] or result == [3, 2]
    
    def test_same_number_twice(self):
        """Test when the same number appears twice and adds up to target."""
        nums = [3, 2, 4, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        # Check that the result is valid (any valid pair)
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_consecutive_numbers(self):
        """Test with consecutive numbers."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 19
        result = self.solution.twoSum(nums, target)
        assert result == [8, 9] or result == [9, 8] 
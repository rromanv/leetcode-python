import pytest
import sys
import os

# Add the parent directory to the path so we can import from problems
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from problems.problem_9 import Solution


class TestPalindromeNumber:
    """Test cases for the isPalindrome function."""
    
    def setup_method(self):
        """Set up the Solution instance for each test."""
        self.solution = Solution()
    
    def test_positive_palindrome(self):
        """Test a positive palindrome number."""
        x = 121
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_positive_non_palindrome(self):
        """Test a positive non-palindrome number."""
        x = 123
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_negative_number(self):
        """Test a negative number (should be False)."""
        x = -121
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_single_digit(self):
        """Test a single digit number."""
        x = 5
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_zero(self):
        """Test zero."""
        x = 0
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_two_digit_palindrome(self):
        """Test a two-digit palindrome."""
        x = 11
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_two_digit_non_palindrome(self):
        """Test a two-digit non-palindrome."""
        x = 12
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_three_digit_palindrome(self):
        """Test a three-digit palindrome."""
        x = 131
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_three_digit_non_palindrome(self):
        """Test a three-digit non-palindrome."""
        x = 132
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_four_digit_palindrome(self):
        """Test a four-digit palindrome."""
        x = 1221
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_four_digit_non_palindrome(self):
        """Test a four-digit non-palindrome."""
        x = 1234
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_large_palindrome(self):
        """Test a large palindrome number."""
        x = 12321
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_large_non_palindrome(self):
        """Test a large non-palindrome number."""
        x = 12345
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_even_digit_palindrome(self):
        """Test a palindrome with even number of digits."""
        x = 123321
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_odd_digit_palindrome(self):
        """Test a palindrome with odd number of digits."""
        x = 12321
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_negative_single_digit(self):
        """Test a negative single digit."""
        x = -5
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_negative_two_digit(self):
        """Test a negative two-digit number."""
        x = -11
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_ending_with_zero(self):
        """Test a number ending with zero (not a palindrome)."""
        x = 10
        result = self.solution.isPalindrome(x)
        assert result == False
    
    def test_multiple_zeros(self):
        """Test a number with multiple zeros."""
        x = 1001
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_all_same_digits(self):
        """Test a number with all same digits."""
        x = 999
        result = self.solution.isPalindrome(x)
        assert result == True
    
    def test_alternating_digits(self):
        """Test a number with alternating digits."""
        x = 1212
        result = self.solution.isPalindrome(x)
        assert result == False 
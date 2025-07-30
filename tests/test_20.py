import pytest
import sys
import os

# Add the parent directory to the path so we can import from problems
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from problems.problem_20 import Solution


class TestValidParentheses:
    """Test cases for the isValid function."""
    
    def setup_method(self):
        """Set up the Solution instance for each test."""
        self.solution = Solution()
    
    def test_simple_valid_parentheses(self):
        """Test simple valid parentheses."""
        s = "()"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_simple_valid_brackets(self):
        """Test simple valid brackets."""
        s = "[]"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_simple_valid_braces(self):
        """Test simple valid braces."""
        s = "{}"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_nested_valid_parentheses(self):
        """Test nested valid parentheses."""
        s = "({})"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_multiple_nested_valid(self):
        """Test multiple nested valid parentheses."""
        s = "([{}])"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_consecutive_valid_pairs(self):
        """Test consecutive valid pairs."""
        s = "()[]{}"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_mixed_valid_combinations(self):
        """Test mixed valid combinations."""
        s = "({[]})"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_single_open_parenthesis(self):
        """Test single open parenthesis."""
        s = "("
        result = self.solution.isValid(s)
        assert result == False
    
    def test_single_close_parenthesis(self):
        """Test single close parenthesis."""
        s = ")"
        result = self.solution.isValid(s)
        assert result == False
    
    def test_mismatched_parentheses(self):
        """Test mismatched parentheses."""
        s = "(]"
        result = self.solution.isValid(s)
        assert result == False
    
    def test_mismatched_brackets(self):
        """Test mismatched brackets."""
        s = "[)"
        result = self.solution.isValid(s)
        assert result == False
    
    def test_mismatched_braces(self):
        """Test mismatched braces."""
        s = "{]"
        result = self.solution.isValid(s)
        assert result == False
    
    def test_wrong_order(self):
        """Test wrong order of brackets."""
        s = "([)]"
        result = self.solution.isValid(s)
        assert result == False
    
    def test_multiple_open_brackets(self):
        """Test multiple open brackets without closing."""
        s = "((("
        result = self.solution.isValid(s)
        assert result == False
    
    def test_multiple_close_brackets(self):
        """Test multiple close brackets without opening."""
        s = ")))"
        result = self.solution.isValid(s)
        assert result == False
    
    def test_empty_string(self):
        """Test empty string."""
        s = ""
        result = self.solution.isValid(s)
        assert result == True
    
    def test_complex_valid_expression(self):
        """Test complex valid expression."""
        s = "({[]})()[]{}"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_complex_invalid_expression(self):
        """Test complex invalid expression."""
        s = "({[}])"
        result = self.solution.isValid(s)
        assert result == False
    
    def test_alternating_valid_pairs(self):
        """Test alternating valid pairs."""
        s = "(){}[]"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_deep_nesting(self):
        """Test deeply nested valid parentheses."""
        s = "((((()))))"
        result = self.solution.isValid(s)
        assert result == True
    
    def test_mixed_deep_nesting(self):
        """Test mixed deeply nested valid parentheses."""
        s = "(([{}]))"
        result = self.solution.isValid(s)
        assert result == True 
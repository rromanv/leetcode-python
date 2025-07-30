import pytest
import sys
import os

# Add the parent directory to the path so we can import from problems
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from problems.problem_3136 import Solution


class TestValidWord:
    """Test cases for the isValid function."""
    
    def setup_method(self):
        """Set up the Solution instance for each test."""
        self.solution = Solution()
    
    def test_valid_word_with_vowels_and_consonants(self):
        """Test a valid word with both vowels and consonants."""
        word = "hello"
        result = self.solution.isValid(word)
        assert result == True
    
    def test_valid_word_with_digits(self):
        """Test a valid word that includes digits."""
        word = "hello123"
        result = self.solution.isValid(word)
        assert result == True
    
    def test_word_too_short(self):
        """Test a word that is too short (less than 3 characters)."""
        word = "hi"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_word_only_vowels(self):
        """Test a word that contains only vowels."""
        word = "aeiou"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_word_only_consonants(self):
        """Test a word that contains only consonants."""
        word = "bcdfg"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_word_with_special_characters(self):
        """Test a word that contains special characters."""
        word = "hello!"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_word_with_spaces(self):
        """Test a word that contains spaces."""
        word = "hello world"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_word_only_digits(self):
        """Test a word that contains only digits."""
        word = "12345"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_mixed_case_word(self):
        """Test a word with mixed case letters."""
        word = "HeLLo123"
        result = self.solution.isValid(word)
        assert result == True
    
    def test_word_with_uppercase_vowels(self):
        """Test a word with uppercase vowels."""
        word = "HELLO"
        result = self.solution.isValid(word)
        assert result == True
    
    def test_word_with_uppercase_consonants(self):
        """Test a word with uppercase consonants."""
        word = "WORLD"
        result = self.solution.isValid(word)
        assert result == True
    
    def test_minimum_length_word(self):
        """Test a word with exactly 3 characters."""
        word = "abc"
        result = self.solution.isValid(word)
        assert result == True
    
    def test_empty_string(self):
        """Test an empty string."""
        word = ""
        result = self.solution.isValid(word)
        assert result == False
    
    def test_single_character(self):
        """Test a single character."""
        word = "a"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_two_characters(self):
        """Test two characters."""
        word = "ab"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_word_with_underscore(self):
        """Test a word that contains underscore."""
        word = "hello_world"
        result = self.solution.isValid(word)
        assert result == False
    
    def test_word_with_hyphen(self):
        """Test a word that contains hyphen."""
        word = "hello-world"
        result = self.solution.isValid(word)
        assert result == False 
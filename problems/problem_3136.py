class Solution:
    def isValid(self, word: str) -> bool:
        """
        3136. Valid Word
        
        https://leetcode.com/problems/valid-word/
        
        Difficulty: Easy
        
        A word is considered valid if:
        1. It contains at least 3 characters
        2. It contains at least one vowel and one consonant
        3. It contains only letters and digits
        
        Algorithm: Single pass validation with a vowels set
        Time Complexity: O(n) - Single pass through the string
        Space Complexity: O(1) - Fixed size vowel set and counters
        """
        if len(word) < 3:
            return False

        vowels = set('aeiou')
        vowel_count = 0
        consonant_count = 0

        for char in word:
            if not char.isalnum():
                return False

            if char.isalpha():
                if char.lower() in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        
        return vowel_count >= 1 and consonant_count >= 1

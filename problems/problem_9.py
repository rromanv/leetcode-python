class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        9. Palindrome Number
        
        https://leetcode.com/problems/palindrome-number/
        
        Difficulty: Easy
        
        Given an integer x, return true if x is a palindrome, and false otherwise.
        
        A number is a palindrome when it reads the same backward as forward.
        For example, 121 is a palindrome, while 123 is not.
        
        Note: Negative numbers are not palindromes.
        
        Algorithm: Two pointers
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        s = str(x)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True 
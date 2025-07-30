class Solution:
    def isValid(self, s: str) -> bool:
        """
        20. Valid Parentheses
        
        https://leetcode.com/problems/valid-parentheses/
        
        Difficulty: Easy
        
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
        determine if the input string is valid.
        
        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
        
        Algorithm: To be implemented
        Time Complexity: To be implemented
        Space Complexity: To be implemented
        """
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        } 

        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False

                last_open = stack.pop()

                if bracket_map[char] != last_open:
                    return False
        
        return len(stack) == 0
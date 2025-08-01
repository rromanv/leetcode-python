from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        56. Merge Intervals
        
        https://leetcode.com/problems/merge-intervals/
        
        Difficulty: Medium
        
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
        and return an array of the non-overlapping intervals that cover all the intervals in the input.
        
        Algorithm: Sort and Merge        
        Time Complexity: O(n log n) - dominated by sorting
        Space Complexity: O(n) - worst case when no intervals overlap
        """
        if not intervals:
            return []

        START, END = 0, 1

        intervals.sort(key=lambda x: x[START])

        result = [intervals[0]]

        for current in intervals[1::]:
            last = result[-1]

            if current[START] <= last[END]:
                last[END] = max(current[END], last[END])
            else:
                result.append(current)
        
        return result
'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.'''
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_index, right_index = 0, len(heights) - 1
        maximum_area = 0

        while left_index < right_index:
            width = right_index - left_index
            min_height = min(heights[left_index], heights[right_index])
            current_area = width * min_height
            maximum_area = max(maximum_area, current_area)

            
            if heights[left_index] < heights[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return maximum_area

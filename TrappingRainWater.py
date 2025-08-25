"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped."""
class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height)-1 
        maxleft=0
        maxright=0
        water=0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    water+=maxleft - height[left]
                left+=1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    water+=maxright - height[right]
                right-=1
        return water 
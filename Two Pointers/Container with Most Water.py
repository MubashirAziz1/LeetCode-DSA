class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        m_area = 0
        while left < right:
            if min(height[left] , height[right]) * (right-left)> m_area:
                m_area = min(height[left] , height[right]) * (right-left)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m_area
            
        

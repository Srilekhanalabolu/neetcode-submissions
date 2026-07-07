class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxarea=0
        i=0
        j=n-1
        while(i<j):
            width=j-i
            height=min(heights[i],heights[j])
            area=width*height
            maxarea=max(maxarea,area)  
            if heights[i] > heights[j]:
                j -= 1   # ✅ move left
            else:
                i += 1   # ✅ move right
        return maxarea     
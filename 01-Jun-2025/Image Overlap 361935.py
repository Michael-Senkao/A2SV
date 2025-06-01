# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
    
        # Get all coordinates of 1s in img1 and img2
        ones_img1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones_img2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        
        translation_count = defaultdict(int)
        
        for x1, y1 in ones_img1:
            for x2, y2 in ones_img2:
                dx = x2 - x1
                dy = y2 - y1
                translation_count[(dx, dy)] += 1
        
        # Return the maximum count, or 0 if no overlap
        return max(translation_count.values(), default=0)
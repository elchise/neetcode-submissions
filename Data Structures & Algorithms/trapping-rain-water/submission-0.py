class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        curl = height[l]
        curr = height[r]       
        maxl = curl
        maxr = curr

        water = 0

        while l < r:
            if curl < curr:
                l += 1
                curl = height[l]
                if curl < maxl:
                    water += (maxl-curl)
                else:
                    maxl = curl
            
            else:
                r -= 1
                curr = height[r]
                if curr < maxr:
                    water += (maxr-curr)
                else:
                    maxr = curr
        
        return water

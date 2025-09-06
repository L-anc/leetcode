class Solution:
    def trap(self, height: list[int]) -> int:
        # a pit has concavity: numbers decrease
        # then increase again
        # save indices with nothing greater than them in 1+ directions

        # squeeze max plateaus
        max_height = max(height)
        i = 0
        while i < len(height) -1:
            if height[i] == max_height and height[i+1] == max_height:
                height.pop(i+1)
            else:
                i += 1

        # detect if only slope
        all_slopes = True
        i = 0
        while i < len(height) - 1:
            if height[i] >= height[i+1]:
                i += 1
            else:
                all_slopes = False
                break
        
        i = 0
        while i < len(height) - 1:
            if height[i] <= height[i+1]:
                i += 1
            else:
                all_slopes = False
                break
        
        if all_slopes:
            return 0
        
        # pad for maxima identification
        height = [0] + height + [0]

        maxima = []
        # identify pits
        for i in range(1, len(height)):
            left = False
            right = False

            j = i
            while j >= 0:
                j -= 1
                if height[j] > height[i]:
                    left = True
                    break
            
            j = i
            while j < len(height)-1:
                j += 1
                if height[j] > height[i]:
                    right = True
                    break

            if not (left and right) and height[i] > 0:
                maxima.append(i)

        vol = 0
        # calculate their volumes
        for i in range(len(maxima)-1):
            pit = height[maxima[i]:maxima[i+1]+1]
            print(f"pit from {maxima[i]} to {maxima[i+1]}: {pit}")
            max_height = min(pit[0], pit[-1])
            for pixl in pit:
                if pixl < max_height:
                    vol += max_height - pixl
        
        return vol
    
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
# print(sol.trap([4,2,3]))  # Output: 1
print(sol.trap([4,2,0,3,2,5]))  # Output: 9
print(sol.trap([4,4,2,0,3,2,5]))  # Output: 9
# print(sol.trap([4,4,4]))  # Output: 0
print(sol.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))  # Output: 83
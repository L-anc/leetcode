class Solution:
    def trap(self, height: list[int]) -> int:
        # a pit has concavity: numbers decrease
        # then increase again
        # use deltas
        
        # pad for maxima identification
        height = [0] + height + [0]

        maxima = []
        # identify pits
        begin = True
        i = 1
        while i < len(height)-1:
            # find maxima
            if begin and height[i-1] <= height[i] > height[i+1]:
                maxima.append(i)
                print(f"maxima found at {i} with height {height[i]}")
                begin = False
            
            elif not begin and height[i-1] < height[i] >= height[i+1]:
                maxima.append(i)
                print(f"maxima found at {i} with height {height[i]}")
                begin = True

            i += 1

        # sanitize maxima
        i = 1
        while i < len(maxima)-1:
            if height[maxima[i]] < height[maxima[i-1]] and height[maxima[i]] < height[maxima[i+1]]:
                maxima.pop(i)
            else:
                i += 1

        print(f"maxima: {maxima}")

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
class Solution:
    def largestHelper(self, lst: list[int]) -> int:
        if lst:
            lstMin = min(lst)
            lstMinIdx = lst.index(lstMin)
            branch1 = self.largestHelper(lst[:lstMinIdx])
            branch2 = self.largestHelper(lst[lstMinIdx + 1:])
            return max(branch1, branch2, lstMin * len(lst))         

        return 0
    
    def largestRectangleArea(self, heights: list[int]) -> int:
        # binary tree, each node is the sublist left or right
        # of the min. In order to cont branch, node max area > parent
        # max area given i & j = min of heights[i:j] * j-i

        # works but memory intensive
        return self.largestHelper(heights)
    
    def largestRectangleArea2(self, height: list[int]) -> int:
        # start at max point, search right and left
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            print(f'--------------{i}')
            print(f"stack {stack}")
            print(height[i])
            print(height[stack[-1]])
            while height[i] < height[stack[-1]]:
                print("True")
                h = height[stack.pop()]
                print(f"h: {h}")
                print(f"stack post pop: {stack}")
                w = i - stack[-1] - 1
                print(f"stack end: {stack[-1]}") 
                print(f"w: {w}")
                print(f"curRect: {h*w}")
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

sol = Solution()
print(sol.largestRectangleArea2([2,1,5,6,2,3]))
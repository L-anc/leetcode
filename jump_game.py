class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Check if there exists a path from j to i
        # and shift i -> j if so
        # O(n) time complexity, O(1) space complexity
                 
        valid = True
        start = 0
        goal = len(nums)-1

        i = goal
        j = goal
        while i > start:
            j -= 1
            if j < start:
                return valid
            
            if nums[j] < i - j:
                valid = False
            else:
                i = j
                valid = True

        return valid  

    # Allthough both functions have O(n) time complexity and O(1) space complexity,
    # this is shorter and easier to understand.
    def canJump2(self, nums: list[int]) -> bool:
        # Greedy approach
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= len(nums) - 1:
                return True
        return False        
    
sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))
print(sol.canJump([2, 5, 0, 0]))
print(sol.canJump([1,1,1,0]))
print(sol.canJump([0, 1, 2, 3]))  # Expected output: False (cannot jump over the first 0)
print(sol.canJump([2,0,1,0,1]))  # Expected output: False (cannot jump over the last 0)
print(sol.canJump([5,0,1,0,1]))  # Expected output: True (cannot jump over the last 0)

print("-----------------")
# compare with canJump2
print(sol.canJump2([2, 3, 1, 1, 4]))  # Expected output: True
print(sol.canJump2([2, 5, 0, 0]))      # Expected output: True
print(sol.canJump2([1, 1, 1, 0]))      # Expected output: True
print(sol.canJump2([0, 1, 2, 3]))      # Expected output: False
print(sol.canJump2([2, 0, 1, 0, 1]))   # Expected output: False
print(sol.canJump2([5, 0, 1, 0, 1]))   # Expected output: True
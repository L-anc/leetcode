class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        i = int(len(nums)/2)
        j = i
        print(i)
        print(j)
        if len(nums) % 2 == 0:
            i -= 1

        print(i)
        print(j)
        
        while i >= 0 and nums[i] <= nums[j]:
            i -= 1
            j += 1
            if i < 0:
                return True
        
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j += 1
            if i < 0:
                return True

        return False
    
sol = Solution()
print(sol.isMonotonic([1,2,2,3]))
print(sol.isMonotonic([6,5,4,4]))
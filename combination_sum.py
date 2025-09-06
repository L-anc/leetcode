class Solution:
    def DFS(self, sum : int, target : int, out : list[list[int]], stack : list[int], nodes: list[int]):
        # Implement DFS
        if sum == target and (sorted(stack) not in out):
            print("Found:", stack)
            copy = [x for x in stack]
            out.append(sorted(copy))
            print("out:", out)
            return
        
        for num in nodes:
            if sum + num <= target:
                stack.append(num)
                sum += num
                self.DFS(sum, target, out, stack, nodes)
                sum -= num
                stack.pop()

        return
        

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        sum = 0
        stack = []
        out = []
        self.DFS(sum, target, out, stack, candidates)
        return out
    
    # Faster and more efficient solution by removing index from candidates at
    # each recursive call
    def dfs(self, nums, target, path, ret):
        print("nums:", nums, "target:", target, "path:", path, "ret:", ret)
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)

    def combinationSum2(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))  # Expected output: [[2, 2, 3], [7]]
print(sol.combinationSum([2, 3, 5], 8))      # Expected output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(sol.combinationSum([1], 1))            # Expected output: [[1]]
print(sol.combinationSum([1], 2))            # Expected output: [[1, 1]]
print(sol.combinationSum([2], 1))            # Expected output: [] (no combinations possible)
print(sol.combinationSum([8,7,4,3], 11))
print("-----------------")
# compare with combinationSum2
print(sol.combinationSum2([2, 3, 6, 7], 7))  # Expected output: [[2, 2, 3], [7]]
print(sol.combinationSum2([2, 3, 5], 8))      # Expected output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(sol.combinationSum2([1], 1))            # Expected output: [[1]]
print(sol.combinationSum2([1], 2))            # Expected output: [[1, 1]]
print(sol.combinationSum2([2], 1))            # Expected output: [] (no combinations possible)
print(sol.combinationSum2([8,7,4,3], 11))
class Solution:
    def convert(self, s: str) -> int:
        match s:
            case "I":
                return 1
            case "V":
                return 5
            case "X":
                return 10
            case "L":
                return 50
            case "C":
                return 100
            case "D":
                return 500
            case "M":
                return 1000
            case _:
                return 0

    def romanToInt(self, s: str) -> int:
        # use hierarchy and order
        sum = 0
        for i in range(len(s)):
            cur = self.convert(s[i])
            if i + 1 < len(s):
                next = self.convert(s[i+1])
                if cur < next:
                    sum -= cur
                    continue
                    
            sum += cur
        return sum
    
sol = Solution()
print(sol.romanToInt("III"))  # Expected output: 3
print(sol.romanToInt("MCMXCIV"))   # Expected output: 1994
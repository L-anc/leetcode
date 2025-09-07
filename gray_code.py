class Solution:
    # @return a list of integers
    '''
    At each step the array is reversed and 2^i is added
    to each number in a new array that is then appended
    e.g.
    for i = 2
    have i = 1: [0, 1, 3, 2]
    add 2^2 = 4 to each index of reversed list [2, 3, 1, 0]: [6, 7, 5, 4]
    concat lists to get i=2: [0, 1, 3, 2 ,6, 7, 5, 4]
    

    start:      [0]
                [0]
    i = 0:      [0, 1]
                [0, 1]
    i = 1:      [0, 1, 3, 2]
                [00, 01, 11, 10]
    i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
                [000, 001, 011, 010, 110, 111, 101, 100]
    '''
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
            print(results)
            print(list(map(lambda num: bin(num)[2:].zfill(n), results)))
        return results
    
sol = Solution()
sol.grayCode(3)
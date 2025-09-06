class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # can get median by getting middle index of sorted arr
        # binary search method for merge?
        final = []

        # demo merge
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                final.append(nums1[0])
                nums1.pop(0)
            else:
                final.append(nums2[0])
                nums2.pop(0)

        if nums1:
            final += nums1
        if nums2:
            final += nums2

        if len(final)%2 == 0:
            print("even")
            return (final[int(len(final)/2 - 1)] + final[int(len(final)/2)]) / 2
        else:
            print("odd")
            print(final)
            return final[int(len(final)/2)]

sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))  # Expected output: 2.0
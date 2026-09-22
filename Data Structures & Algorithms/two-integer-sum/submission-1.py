class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        #sorts by first element
        A.sort()
        #intialize the points i, j
        i, j = 0, len(nums) - 1
        while i < j:
            #[0] returns only the values with no index indices
            cur = A[i][0] + A[j][0]
            if cur == target:
                #[1] returns the indicies now
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
        
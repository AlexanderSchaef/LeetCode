class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i):
                if i == 0:
                    pass
                elif nums[i] < nums[j]:
                    if not (str(bin(nums[i])).count("1") == str(bin(nums[j])).count("1")):
                        return False
        return True


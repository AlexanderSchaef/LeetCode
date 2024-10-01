"""
Alexander Schaefer
10/01/24
"""

class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]






if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution.twoSum(nums, target) == [0,1])
    nums = [3,2,4]
    target=6
    print(Solution.twoSum(nums, target) == [1,2])
    nums=[3,3]
    target=6
    print(Solution.twoSum(nums, target) == [0,1])

    print("All test cases passed. Question solved.")
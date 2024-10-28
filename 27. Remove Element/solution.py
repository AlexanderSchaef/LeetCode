class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i, e in enumerate(nums):
            if nums[i] == val:
                count = count + 1
        for i in range(count):
            nums.remove(val)
        for i in range(count):
            nums.append(val)
        count = 0
        for num in nums:
            if num != val:
                count = count + 1
        return count
        

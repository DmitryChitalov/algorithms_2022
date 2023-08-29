
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last = nums[0]
        l_index = 1
        for r_index in range(1, len(nums)):
            if nums[r_index] != last:
                last = nums[r_index]
                nums[l_index] = nums[r_index]
                l_index += 1
        return l_index

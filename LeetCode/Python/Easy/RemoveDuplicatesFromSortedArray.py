# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = []
        uniquePointer = 0

        for index, num in enumerate(nums):
            if num not in uniqueNums:
                uniqueNums.append(num)
                nums[uniquePointer] = num
                uniquePointer += 1

        return len(uniqueNums)

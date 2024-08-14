# Problem link: https://leetcode.com/problems/two-sum/

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for index in range(0, len(nums)):
      currentNumber = nums[index]

      for index2 in range(index + 1, len(nums)):
        nextNumber = nums[index2]

        if currentNumber + nextNumber == target:
          return [index, index2]

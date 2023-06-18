// https://leetcode.com/problems/two-sum/description/

const twoSum = function(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    const currentNumber = nums[i];

    for (let j = i + 1; j < nums.length; j++) {
      const nextNumber = nums[j];

      if (currentNumber + nextNumber === target && i !== j) {
        return [i, j];
      }
    }
  }
};

[2,7,11,15]
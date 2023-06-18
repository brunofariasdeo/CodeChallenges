// URL: https://leetcode.com/problems/contains-duplicate/

const containsDuplicate = function (nums) {
    numbersObject = {}

    for (let i=0; i<nums.length; i++) {
        if(numbersObject[nums[i]]) {
            numbersObject[nums[i]]+=1;
        }
        else {
            numbersObject[nums[i]]=1;
        }
    }

    for (const [_, value] of Object.entries(numbersObject)) {
        if (value > 1) {
            return true
        }
    }

    return false
};

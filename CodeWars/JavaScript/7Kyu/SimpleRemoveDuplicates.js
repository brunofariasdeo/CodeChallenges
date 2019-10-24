// URL: https://www.codewars.com/kata/simple-remove-duplicates/train/javascript

function solve(arr){
  let numbersFound = [];
  arr.reverse()

  console.log(arr);

  for (i=0;i<arr.length;i++){
    if (!numbersFound.includes(arr[i])){
      numbersFound.push(arr[i]);
    }
  }

  return numbersFound.reverse();
}

console.log(solve([3,4,4,3,6,3]));
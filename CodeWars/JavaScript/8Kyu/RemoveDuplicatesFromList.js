// URL: https://www.codewars.com/kata/remove-duplicates-from-list/train/javascript

function distinct(a) {
  return [...new Set(a)];
}

console.log(distinct([1,2,2,3,4,4]));
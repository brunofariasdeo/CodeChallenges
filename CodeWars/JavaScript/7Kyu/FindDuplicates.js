// URL: https://www.codewars.com/kata/find-duplicates/train/javascript

function duplicates(arr) {
  let duplicatesList= [];
  let numbersFound= [];

  for (i=0;i<arr.length;i++){
    if ((numbersFound.includes(arr[i])) && (!duplicatesList.includes(arr[i]))){
      duplicatesList.push(arr[i]);
      }
    else{
      numbersFound.push(arr[i]);
      }
    }
    
  return duplicatesList
}

console.log(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']));
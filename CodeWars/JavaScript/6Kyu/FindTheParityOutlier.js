// URL: https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/javascript

function findOutlier(integers){
  const integersArray = integers.filter(integer => integer%2 === 0);
  
  return integersArray.length === 1 ?
    integersArray[0] :
    integers.filter(integer => integer%2 !== 0)[0]
}
// URL: https://www.codewars.com/kata/simple-fun-number-10-range-bit-counting/train/javascript

function rangeBitCount(a, b) {
  let count = 0
  
  for (i=a;i<=b;i++){
    let number = parseInt(i, 10).toString(2)
    
    for (j=0;j<number.length;j++){
      if (number[j] == 1){
        count+=1;
      }
    }
  }
  
  console.log(count)
  return count
}

rangeBitCount(2,7)
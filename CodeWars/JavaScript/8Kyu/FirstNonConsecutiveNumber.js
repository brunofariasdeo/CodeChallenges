// URL: https://www.codewars.com/kata/find-the-first-non-consecutive-number/train/javascript

function firstNonConsecutive (arr) {
    for (i=0;i<arr.length;i++){
      if (i>0){
        if (arr[i] !== arr[i-1]+1){
          return arr[i]
        }
      }
    }
    
    return null
  
  }
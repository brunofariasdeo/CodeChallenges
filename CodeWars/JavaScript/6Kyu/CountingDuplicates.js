// URL: https://www.codewars.com/kata/counting-duplicates/train/javascript

function duplicateCount(text){
  let textArray = text.toUpperCase().split('');
  let countLetters = {};
  let sum = 0;
  
  for (let i = 0; i < textArray.length; i++) {
    let num = textArray[i];
    countLetters[num] = countLetters[num] ? countLetters[num] + 1 : 1;
  }

  for(var key in countLetters) {
    if (!(countLetters[key] == 1)){
      sum+=1
    }
  }
  
  return sum;
}
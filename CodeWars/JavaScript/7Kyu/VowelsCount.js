// URL: https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/javascript

function getCount(str) {
  let vowelsCount = 0;
  const vowels = ['a','e','i','o','u'];
  
  for (let i=0; i<str.length; i++){
    if (vowels.includes(str[i])){
      vowelsCount += 1;
    } 
  }
  
  return vowelsCount;
}
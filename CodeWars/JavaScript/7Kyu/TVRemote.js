// URL: https://www.codewars.com/kata/tv-remote/train/javascript

var tvRemote = function(word) {
  const remoteControlKeyboard= ["abcde123","fghij456","klmno789","pqrst.@0","uvwxyz_/"];

  let current = [0,0];
  let stepsRequired = [];

  for (i=0;i<word.length;i++){
    for (j=0;j<remoteControlKeyboard.length;j++){
      if (remoteControlKeyboard[j].includes(word[i])){
        stepsRequired.push((Math.abs(current[0] - remoteControlKeyboard[j].indexOf(word[i]))) + (Math.abs(current[1] - j)) + 1);
        current[0] = remoteControlKeyboard[j].indexOf(word[i]);
        current[1] = j;
      }
    }
  }
  return stepsRequired.reduce((a,b)=>a+b,0);

}

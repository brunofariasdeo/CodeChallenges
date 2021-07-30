// URL: https://www.codewars.com/kata/59377c53e66267c8f6000027/train/javascript

function alphabetWar(fight){
  alphabet = {
    "left":{
      "w":4,
      "p": 3,
      "b": 2,
      "s": 1
    },
    "right":{
      "m":4,
      "q":3,
      "d":2,
      "z":1
    }
  }
  
  left = 0
  right = 0
  
  for (let i=0; i<fight.length; i++){
    if(fight[i] in alphabet.left){
      left += alphabet.left[fight[i]];
    }
    else if (fight[i] in alphabet.right){
      right += alphabet.right[fight[i]];
    }
  }
  
  if (right>left){
    return "Right side wins!";
  }
  else if(left===right){
    return "Let's fight again!";
  }
  else{
    return "Left side wins!";
  }
}

console.log(alphabetWar("tsqwpmsasm"));
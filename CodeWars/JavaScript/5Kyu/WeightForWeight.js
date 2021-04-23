// URL: https://www.codewars.com/kata/55c6126177c9441a570000cc/train/javascript

function orderWeight(strng) {
  let stringList = strng.split(" ");

  let sumDigitsList = stringList.map(
    number => number.split('')
        .map(Number)
        .reduce(function (a, b) {
            return a + b;
        }, 0)
  );

  let stringObject = {}

  for (let i=0; i<stringList.length; i++){
    if(stringObject.hasOwnProperty(sumDigitsList[i])){
      stringObject[sumDigitsList[i]].push(stringList[i])
    }
    else{
      stringObject[sumDigitsList[i]] = [stringList[i]];
    }
  }

  for(let prop in stringObject){
    stringObject[prop].sort();
  }

  let finalList = [];

  for(let prop in stringObject){
    finalList.push.apply(finalList, stringObject[prop]);
  }
  
  return finalList.join(' ');
}

console.log(orderWeight("56 65 74 100 99 68 86 180 90"));
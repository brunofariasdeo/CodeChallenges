// URL: https://www.codewars.com/kata/only-duplicates/train/javascript

function onlyDuplicates(str) {
  let stringList = str.split('');
  let finalString = [];

  for (i=0;i<stringList.length;i++){
    if (!(stringList.slice(i+1,stringList.length).includes(stringList[i])) && !(stringList.slice(0,i).includes(stringList[i]))){
      finalString.push("");
    }
    else{
      finalString.push(stringList[i]);
    }
  }

  return finalString.join('');
}

console.log(onlyDuplicates('abccdefee'));
// URL: https://www.codewars.com/kata/find-the-longest-gap/train/javascript

function gap(num) {
  maxLengthFound = 0;
  string = "";

  binary = num.toString(2);

  for (i=0;i<binary.length;i++){
    if (binary[i] == "1"){
      if (maxLengthFound<string.length){
        maxLengthFound = string.length;
      }
        string = "";
    }
    else{
      string += binary[i];
    }
  }  

  return maxLengthFound;

}

console.log(gap(15));
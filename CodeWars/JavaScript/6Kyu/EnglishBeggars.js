// URL: https://www.codewars.com/kata/english-beggars/train/javascript

function beggars(values, n){
  money = [];
  for (i=0;i<n;i++){
    value = 0;
    
    for(j=i;j<values.length;j+=n){
      if ((j)<values.length){
        value+=values[j];
      }
    }

    money.push(value);
  }

  return money;
}

console.log(beggars([1,2,3,4,5],2));
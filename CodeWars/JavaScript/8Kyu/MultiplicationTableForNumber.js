// URL: https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/javascript

function multiTable(number) {
  let multiplicationTable = [];
  
  for (i=1; i<=10; i++){
    multiplicationTable.push(`${i} * ${number} = ${i*number}`);
  }
  
  return multiplicationTable.join('\n');
}
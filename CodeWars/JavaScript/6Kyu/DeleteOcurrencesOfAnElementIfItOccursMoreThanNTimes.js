// https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/javascript

function deleteNth(arr,n){
  let numbers = {};
  let newArray = [];
  
  for (let i=0; i<arr.length; i++){

    if (arr[i] in numbers){
      numbers[arr[i]] += 1;
    }
    else{
      numbers[arr[i]] = 1;
    }
    
    if(numbers[arr[i]]<=n){
      newArray.push(arr[i]);
    }
  }
    
  return newArray;  
}

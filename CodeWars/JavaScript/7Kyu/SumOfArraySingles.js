// URL = https://www.codewars.com/kata/59f11118a5e129e591000134/train/javascript

function repeats(arr){
    let numbers = {};
    let sum = 0;

    for (let i=0; i<arr.length; i++){
        if (numbers.hasOwnProperty(arr[i])){
            numbers[arr[i]]+=1;
        }
        else{
            numbers[arr[i]]=1;
        }
    }

    for (const [key, value] of Object.entries(numbers)) {
        if (numbers[key] === 1){
            sum+=parseInt(key);
        }
    }

    return sum;
};

console.log(repeats([4,5,7,5,4,8]));
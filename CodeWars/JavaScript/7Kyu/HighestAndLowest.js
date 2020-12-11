// URL: https://www.codewars.com/kata/554b4ac871d6813a03000035/train/javascript

function highAndLow(numbers){
    numbers = numbers.split(" ");
    numbersConverted = numbers.map(number => parseInt(number));
    
    return `${Math.max(...numbersConverted)} ${Math.min(...numbersConverted)}`;
}
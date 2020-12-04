// URL: https://www.codewars.com/kata/5a00e05cc374cb34d100000d?utm_source=newsletter

const reverseSeq = n => {
    let array = [];

    while (n!=0){
        array.push(n);
        n = n-1;
    }

    return array;
};

console.log(reverseSeq(5));
// URL: https://www.codewars.com/kata/593c9175933500f33400003e/train/javascript

function multiples(m, n){
    multiplesArray = [];

    for (let i=n; i<=Math.abs(m*n); i=i+n){
        multiplesArray.push(i)

        if (Math.abs(i) === Math.abs(m*n)){
            break;
        }
    }

    return multiplesArray;
}

console.log(multiples(5, -1));
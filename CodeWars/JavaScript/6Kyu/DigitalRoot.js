// URL: https://www.codewars.com/kata/541c8630095125aba6000c00/train/javascript

function digital_root(n) {
  digitalRootFound = false;

  while(digitalRootFound === false){
    n = n.toString(10).split("").map(function(t){return parseInt(t)});
    n = sum(n);

    if (n.toString().length === 1){
      return n;
    }
  }
}

function sum(n){
  return n.reduce((a, b) => a + b, 0);
}

console.log(digital_root(16));
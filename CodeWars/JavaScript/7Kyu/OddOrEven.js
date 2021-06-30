// URL: https://www.codewars.com/kata/5949481f86420f59480000e7/train/javascript

function oddOrEven(array) {
  const sum = array.reduce((accumulator, currentValue) => {
    return accumulator + currentValue;
  }, 0);

  return sum % 2 == 0 ? 'even' : 'odd';
}

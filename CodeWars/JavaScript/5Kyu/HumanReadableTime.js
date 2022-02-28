// URL: https://www.codewars.com/kata/52685f7382004e774f0001f7/train/javascript

function humanReadable (seconds) {
  const hours = Math.floor(seconds / 3600);
  let secondsRemaining = seconds - (hours * 3600);

  const minutes = Math.floor(secondsRemaining / 60);
  secondsRemaining = secondsRemaining - (minutes * 60);

  return [
    hours.toString().padStart(2, '0'), 
    minutes.toString().padStart(2, '0'), 
    secondsRemaining.toString().padStart(2, '0')
  ].join(':');
}

console.log(humanReadable(0))
console.log(humanReadable(59))
console.log(humanReadable(60))
console.log(humanReadable(90))
console.log(humanReadable(3599))
console.log(humanReadable(3600))
console.log(humanReadable(45296))

// URL: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/javascript

function accum(s) {
  let mumbleString = "";
  
  for (i=0; i<s.length; i++){
    mumbleString += s[i].toUpperCase() + s[i].toLowerCase().repeat(i) + "-";
  }
  
  return mumbleString.slice(0,-1);
}
// URL = https://leetcode.com/problems/valid-parentheses/
const isValid = function(s) {
  let stack = []

  for (char of s){
    if (char === '(' || char === '{' || char === '[') {
      stack.push(char)
    }
    else {
      if (!stack.length === 0) {
        return false
      }

      if (char === ')' && stack[stack.length - 1] === '(') {
        stack.pop()
      }
      else if (char === '}' && stack[stack.length - 1] === '{') {
        stack.pop()
      }
      else if (char === ']' && stack[stack.length - 1] === '[') {
        stack.pop()
      }
      else {
        return false
      }
    }
  }

  return stack.length === 0
};

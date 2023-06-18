// https://leetcode.com/problems/valid-anagram/

const isAnagram = function (s, t) {
  lettersObjectS = {}
  lettersObjectT = {}

  for (const letter of s) {
      if (lettersObjectS[letter]) {
          lettersObjectS[letter] += 1;
      }
      else {
          lettersObjectS[letter] = 1;
      }
  }

  for (const letter of t) {
      if (lettersObjectT[letter]) {
          lettersObjectT[letter] += 1;
      }
      else {
          lettersObjectT[letter] = 1;
      }
  }

  for (const key of Object.keys(lettersObjectS)) {
      const regexPattern = new RegExp(key, "gi");
      const letterCount = (t.match(regexPattern) || []).length;

      if (letterCount !== lettersObjectS[key]) {
          return false;
      }
  }

  for (const key of Object.keys(lettersObjectT)) {
      const regexPattern = new RegExp(key, "gi");
      const letterCount = (s.match(regexPattern) || []).length;

      if (letterCount !== lettersObjectT[key]) {
          return false;
      }
  }

  return true;
};
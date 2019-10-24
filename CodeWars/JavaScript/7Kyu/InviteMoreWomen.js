// URL: https://www.codewars.com/kata/simple-fun-number-152-invite-more-women/train/javascript

function inviteMoreWomen(L) {
  let women = []
  let men = []
  
  for (i=0;i<L.length;i++){
    if (L[i] == "1"){
      men.push(L[i])
    }
    else{
      women.push(L[i])
    }
  }

  if (men.length != women.length && men.length > women.length) {
    return true
  }
  else{
    return false
  }
  
}
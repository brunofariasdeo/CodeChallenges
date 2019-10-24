function isLockNessMonster(s) {
    found = ["tree fiddy", "tree fifty", "3.50"];
    
    if (s.includes(found[0]) || s.includes(found[1]) || s.includes(found[2])){
      return true;
    }
    else{
      return false;
    }
    
  }
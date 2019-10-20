function describeAge(a){
    var f=(a<=12)?"kid":(a>=13&&a<=17)?"teenager":(a>=18&&a<=64)?"adult":"elderly" 
    return "You're a(n) "+f 
  };
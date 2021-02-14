public class SetAlarm {
  
  public static boolean setAlarm(boolean employed, boolean vacation) {
    if (employed && !vacation){
      return true;
    }
    
    return false;
  }

}
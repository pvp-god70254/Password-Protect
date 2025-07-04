import java.io.*;
public class main {
  public static void main(String[] args){
    part1();
    System.out.println("25% done");
    part2();
    System.out.println("50% done");
    part3();
    System.out.println("75% done");
    part4();
    System.out.println("100% done");
  }
  
  public static void part1(){
    int a=-1;
    while ( a < 9 ) {
      a = a + 1;
      String string_A = String.format("%s", a);
      new File(string_A).mkdir();
    }
  }
  
  public static void part2(){
    int a=-1;
    while ( a < 9 ) {
      a = a + 1;
      int b=-1;
      while ( b < 9 ) {
        b = b + 1;
        String string_AB = String.format("%s/%s", a, b);
        new File(string_AB).mkdir();
      }
    }
  }
  
  public static void part3(){
    int a=-1;
    while ( a < 9 ) {
      a = a + 1;
      int b=-1;
      while ( b < 9 ) {
        b = b + 1;
        int c=-1;
        while ( c < 9 ){
          c = c + 1;
          String string_ABC = String.format("%s/%s/%s", a, b, c);
          new File(string_ABC).mkdir();
        }
      }
    }
  }
  
  public static void part4(){
    int a=-1;
    while ( a < 9 ) {
      a = a + 1;
      int b=-1;
      while ( b < 9 ) {
        b = b + 1;
        int c=-1;
        while ( c < 9 ){
          c = c + 1;
          int d=-1;
          while ( d < 9 ){
            d = d + 1;
            String string_ABCD = String.format("%s/%s/%s/%s", a, b, c, d);
            String file = String.format("%s/%s/%s/%s/.combo", a, b, c, d);
            new File(string_ABCD).mkdir();
            new File(file).createNewFile();
          }
        }
      }
    }
  }
}
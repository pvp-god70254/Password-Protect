package main

import "fmt"
import "os"

func part1() {
    var a int = -1
    for a < 9 {
      a = a + 1
      var string_a string = fmt.Sprintf("%d", a)
      os.Mkdir(string_a, 0755)
    }
}

func part2() {
    var a int = -1
    for a < 9 {
      a = a + 1
      var b int = -1
      for b < 9 {
        b = b + 1
        var string_ab string = fmt.Sprintf("%d/%d", a, b)
        os.Mkdir(string_ab, 0755)
      } 
    }
}

func part3() {
    var a int = -1
    for a < 9 {
      a = a + 1
      var b int = -1
      for b < 9 {
        b = b + 1
        var c int = -1
        for c < 9 {
          c = c + 1
          var string_abc string = fmt.Sprintf("%d/%d/%d", a, b, c)
          os.Mkdir(string_abc, 0755)
        } 
      } 
    }
}

func part4() {
    var a int = -1
    for a < 9 {
      a = a + 1
      var b int = -1
      for b < 9 {
        b = b + 1
        var c int = -1
        for c < 9 {
          c = c + 1
          var d int = -1
          for d < 9 {
            d = d + 1
            var string_abcd string = fmt.Sprintf("%d/%d/%d/%d", a, b, c, d)
            var filename string = fmt.Sprintf("%d/%d/%d/%d/.combo", a, b, c, d)
            os.Mkdir(string_abcd, 0755)
            os.Create(filename)
        } 
        } 
      } 
    }
}

func main() {
  part1()
  fmt.Println("25% complete")
  part2()
  fmt.Println("50% complete")
  part3()
  fmt.Println("75% complete")
  part4()
  fmt.Println("100% complete")
}
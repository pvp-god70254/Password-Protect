const process = require('process');
const fs = require('fs')

function part1(){
  for (var a = 0; a <= 9; a++){
    fs.mkdirSync(String(a))
  }
}

function part2(){
  for (var a = 0; a <= 9; a++){
    for (var b = 0; b <= 9; b++){
      fs.mkdirSync(`${String(a)}/${String(b)}`)
    }
  }
}

function part3(){
  for (var a = 0; a <= 9; a++){
    for (var b = 0; b <= 9; b++){
      for (var c = 0; c <= 9; c++){
        fs.mkdirSync(`${String(a)}/${String(b)}/${String(c)}`)
      }
    }
  }
}

function part4(){
  for (var a = 0; a <= 9; a++){
    for (var b = 0; b <= 9; b++){
      for (var c = 0; c <= 9; c++){
        for (var d = 0; d <= 9; d++){
          fs.mkdirSync(`${String(a)}/${String(b)}/${String(c)}/${String(d)}`)
        }
      }
    }
  }
}

function start(){
  part1()
  console.log("25% complete")
  part2()
  console.log("50% complete")
  part3()
  console.log("75% complete")
  part4()
  console.log("100% complete")
}

start()
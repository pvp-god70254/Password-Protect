import os

def mkdir(name):
  os.system(f"mkdir {name}")
  
def cd(newdir):
  os.chdir(str(newdir))
  
initial_directory = os.getcwd()

def part_1():
  a = -1
  while a < 9:
    a = a + 1
    mkdir(a)

def part_2():
  a = -1
  while a < 9:
    a = a + 1
    cd(a)
    b = -1
    while b < 9:
      b = b + 1
      mkdir(b)
    cd("../")
    b = -1
  cd(initial_directory)

def part_3():
  a = -1
  while a < 9:
    a = a + 1
    b = -1
    while b < 9:
      b = b + 1
      cd(f"{a}/{b}")
      c = -1
      while c < 9:
        c = c + 1
        mkdir(c)
      cd(initial_directory)
      c = -1
  cd(initial_directory)
  
def part_4():
  a = -1
  while a < 9:
    a = a + 1
    b = -1
    while b < 9:
      b = b + 1
      c = -1
      while c < 9:
        c = c + 1
        cd(f"{a}/{b}/{c}")
        d = -1
        while d < 9:
          d = d + 1
          mkdir(d)
          os.system(f"touch {d}/.combo")
        cd(initial_directory)
      d = -1
    c = -1
  b = -1
cd(initial_directory)

def start():
  part_1()
  print("25% complete")
  part_2()
  print("50% complete")
  part_3()
  print("75% complete")
  part_4()
  print("100% complete")
  
start()
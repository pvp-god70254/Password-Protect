import os
Languages_Dir = os.getcwd() + "/Languages"
os.system("clear")
print("Password Locker")
print("This script creates 11,110 folders so you can input a code")
print("to get all combos use find */*/*/*/.combo")
print("------------------")
print(" PASSWORD PROTECT ")
print("------------------")
input("press enter key to continue")

os.system("clear")
name = "passwordProtect"

def start():
  print("Dirrectory of the passcode lock")
  dir = input("Directory: ")
  os.system("clear")
  try:
    os.chdir(dir)
    main()
  except Exception:
    os.system(f"mkdir {dir}")
    os.chdir(dir)
    main()

def handle2(ID):
  if ID == "0":
    os.system("clear")
    exit()
  elif ID == "1":
    os.system("clear")
    main()
  elif ID == "2":
    os.system("clear")
    start()
  else:
    os.system("clear")
    print("INVALID OPTION\n")
    more_options()
    
def main():
  print("choose the language")
  print("")
  print("IDS:")
  print("0: more options")
  print("1: node.js (2.536 - 3.672)s")
  print("2: golang (3.452 - 4.261)s")
  print("3: java (8.400 - 9.180)s")
  print("4: c++ (9.006 - 10.786)s")
  print("5: c (9.150 - 11.525s)s")
  print("6: bash (366.543 - 380.8)s")
  print("7: python (601.280 - 603.981)s")
  print("8: lua (621.004 - 628.094)s")
  print("")
  ID = input("language ID: ")
  handle(ID)
  
def handle(ID):
  if ID == "0":
    os.system("clear")
    more_options()
  elif ID == "1":
    os.system("clear")
    os.system(f"node {Languages_Dir}/{name}.js")
  elif ID == "2":
    os.system("clear")
    os.system(f"go run {Languages_Dir}/{name}.go")
  elif ID == "3":
    os.system("clear")
    os.system(f"java {Languages_Dir}/{name}.java")
  elif ID == "4":
    os.system("clear")
    os.system(f"gcc {Languages_Dir}/{name}.cpp -o ~/tmp.gcc.cpp")
    os.system(f"chmod +x ~/tmp.gcc.cpp")
    os.system(f"~/tmp.gcc.cpp")
    os.system(f"rm -r ~/tmp.gcc.cpp")
  elif ID == "5":
    os.system("clear")
    os.system(f"gcc {Languages_Dir}/{name}.c -o ~/tmp.gcc.c")
    os.system(f"chmod +x ~/tmp.gcc.c")
    os.system(f"~/tmp.gcc.c")
    os.system("clear")
    os.system(f"rm -r ~/tmp.gcc.c")
  elif ID == "6":
    os.system("clear")
    os.system(f"sh {Languages_Dir}/{name}.bash")
  elif ID == "7":
    os.system("clear")
    os.system(f"python {Languages_Dir}/{name}.py")
  elif ID == "8":
    os.system("clear")
    os.system(f"lua {Languages_Dir}/{name}.lua")
  else:
    os.system("clear")
    print("INVALID ID")
    print("")
    main()
  
def more_options():
  print("choose your option")
  print("")
  print("0: exit")
  print("1: back to options")
  print("2: change directory")
  print("")
  opt = input("option ID: ")
  handle2(opt)
  

  
start()
function part1()
  a=-1
  while a < 9
  do
    a=a+1
    os.execute(string.format("mkdir %d", a))
  end
end

function part2()
  a=-1
  while a < 9
  do
    a=a+1
    b=-1
    while b < 9
    do
      b=b+1
      os.execute(string.format("mkdir %d/%d", a, b))
    end
  end
end

function part3()
  a=-1
  while a < 9
  do
    a=a+1
    b=-1
    while b < 9
    do
      b=b+1
      c=-1
      while c < 9
      do
        c=c+1
        os.execute(string.format("mkdir %d/%d/%d", a, b, c))
      end
    end
  end
end

function part4()
  a=-1
  while a < 9
  do
    a=a+1
    b=-1
    while b < 9
    do
      b=b+1
      c=-1
      while c < 9
      do
        c=c+1
        d=-1
        while d < 9
        do
          d=d+1
          os.execute(string.format("mkdir %d/%d/%d/%d", a, b, c, d))
          os.execute(string.format("touch %d/%d/%d/%d/.combo", a, b, c, d))
        end
      end
    end
  end
end

function start()
part1()
print("25% done")
part2()
print("50% done")
part3()
print("75% done")
part4()
print("100% done")
end

start()
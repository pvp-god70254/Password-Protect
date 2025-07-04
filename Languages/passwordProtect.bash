part1() {
  a=-1
  while [ "$a" -lt 9 ]; do
    a=$((a + 1))
    mkdir "$a"
  done
}

part2() {
  a=-1
  while [ "$a" -lt 9 ]; do
    a=$((a + 1))
    b=-1
    cd "$a" || return
    while [ "$b" -lt 9 ]; do
      b=$((b + 1))
      mkdir "$b"
    done
    cd ..
  done
}

part3() {
  a=-1
  while [ "$a" -lt 9 ]; do
    a=$((a + 1))
    b=-1
    while [ "$b" -lt 9 ]; do
      b=$((b + 1))
      c=-1
      cd "$a/$b" || return
      while [ "$c" -lt 9 ]; do
        c=$((c + 1))
        mkdir "$c"
      done
      cd ../..
    done
  done
}

part4() {
  a=-1
  while [ "$a" -lt 9 ]; do
    a=$((a + 1))
    b=-1
    while [ "$b" -lt 9 ]; do
      b=$((b + 1))
      c=-1
      while [ "$c" -lt 9 ]; do
        c=$((c + 1))
        d=-1
        cd "$a/$b/$c" || return
        while [ "$d" -lt 9 ]; do
          d=$((d + 1))
          mkdir "$d"
          touch "$d/.combo"
        done
        cd ../../..
      done
    done
  done
}

start() {
  part1
  echo "1/4 done"
  part2
  echo "2/4 done"
  part3
  echo "3/4 done"
  part4
  echo "4/4 done"
}

start
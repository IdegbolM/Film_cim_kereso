def main():
  x=0
  talalat=0
  
  with open('scriptek.txt') as f:
    x = len(f.readlines())

  f.close()

  contents=list()
  with open('scriptek.txt') as fp:
    contents = fp.readlines()

  f.close()

  
  szoveg = input("Kerem a szovegreszletet! (min. 9 karakter, csak kisbetuk) \n")
  while len(szoveg)<=8:
    szoveg = input("Ennel hosszabbat kerek: ")
    
  hossz=len(szoveg)
  for i in range(x):
    jo=0
    if i%2==0:
      print("")
    else:
      for s in range(len(contents[i])):
        if hossz>(len(contents[i])-s):
          s=len(contents[i])
        else:
          while szoveg[jo]==contents[i][s]:
            jo+=1
            s+=1
            if jo==hossz:
              print("Ez a szovegreszlet ebben a filmben talalhato -> "+contents[i-1])
              talalat+=1
              break
        jo=0
        s-=1
        if i==x-1:
          if hossz>(len(contents[i])-s):
            if talalat==0:
              print("Nincs ilyen szovegreszlet!")
              return 0
            else:
              return 0
          
main()
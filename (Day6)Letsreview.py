n = int(input())
for i in range(n):
     string = input()
     estr, ostr = '', ''
     for char in range(len(string)):   
          if char %2 == 0:
               estr += string[char]
          else:
               ostr += string[char]
     print(estr +' '+ ostr)
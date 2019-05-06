cou = 2
plist = [3]
n = 100
for i in range(4,n):
 if(i%2 != 0):
  prime = True
  for pr in plist:
   if(i%pr == 0):
    prime = False
    break
  if(prime):
   plist += [i]
   cou += 1
print(plist)
print(cou)
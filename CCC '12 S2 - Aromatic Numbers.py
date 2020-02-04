aromaticraw = str(input())
rawlst = []
multlst = []

#convert to numeric
for r in aromaticraw:
  if r == "M":
    rawlst.append(1000)
  elif r == "D":
    rawlst.append(500)
  elif r == "C":
    rawlst.append(100)
  elif r == "L":
    rawlst.append(50)
  elif r == "X":
    rawlst.append(10)
  elif r == "V":
    rawlst.append(5)
  elif r == "I":
    rawlst.append(1)  
  else:
    rawlst.append(int(r))

#make lesser values negative 
for n,i in enumerate(rawlst,1):
  if n > 2 and n % 2 == 0:
    if i > rawlst[n-3]:
      rawlst[n-3] = -1 * int(rawlst[n-3])

#apply multiplication
for n,i in enumerate(rawlst,1):
  if n % 2 == 0:
    multlst.append(rawlst[n-2] * i)

#addition/final answer
sumlist = sum(multlst)
print(sumlist)

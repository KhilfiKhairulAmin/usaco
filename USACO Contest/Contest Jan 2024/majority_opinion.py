T = int(input())

cows = []
hays = []
for _ in range(T):
  cows.append(int(input()))
  hays.append([int(h) for h in input().split(" ")])

for _ in range(T):
  out_set = set()

  hay = hays.pop(0)
  
  consec = [hay.pop(0), hay.pop(0)]

  if consec[0] == consec[1]:
    out_set.add(consec[0])

  while len(hay) != 0:
    temp = hay.pop(0)

    if temp in consec:
      out_set.add(temp)

    consec.pop(0)
    consec.append(temp)

  if len(out_set) == 0:
    print("-1")
  else:
    out = list(out_set)
    out.sort()
    for i in range(len(out) - 1):
      print(out[i], end=" ")
    print(out[-1])

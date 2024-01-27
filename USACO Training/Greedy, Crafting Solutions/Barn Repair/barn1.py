"""
ID: khilfik1
LANG: PYTHON3
TASK: barn1
"""
with open("barn1.in") as fileIn:
  M, S, C = (int(x) for x in next(fileIn)[:-1].split(" "))

  barns = []
  for i in range(C):
    barns.append(int(next(fileIn)[:-1]))

  barns.sort()

  barns_ranges = []
  temp = barns[0]
  for i in range(1, C):
    barns_ranges.append((temp, barns[i]))
    temp = barns[i]
  
print("Barns: ", barns)
print("Barns Ranges: ", barns_ranges)

with open("barn1.out", "w") as fileOut:
  out = str(C) + "\n"
  if M == C:
    fileOut.write(out)
    exit()
  elif C == S:
    fileOut.write(out)
    exit()
  
  total_barns = C
  for i in range(C, M, -1):
    temp = barns_ranges[0]
    min_diff = temp[1] - temp[0]
    min_i = 0
    for i in range(1, len(barns_ranges)):
      temp = barns_ranges[i]
      diff = temp[1] - temp[0]
      if diff < min_diff:
        min_diff = diff
        min_i = i
    total_barns += min_diff - 1
    barns_ranges.pop(min_i)

  print("Total Barns: ", total_barns)
  fileOut.write(str(total_barns) + "\n")

"""
ID: khilfik1
LANG: PYTHON3
TASK: milk2
"""
ranges = []
with open("milk2.in") as fileIn:

  n = int(next(fileIn)[:-1])
  for i in range(n):
    ranges.append([int(x) for x in next(fileIn).replace("\n", "").split(" ")])
  ranges.sort(key=lambda x: x[0])

i = 1
while i != len(ranges):
  low_r, high_r = ranges[i]
  if low_r >= ranges[i-1][0] and high_r <= ranges[i-1][1]:
    ranges.pop(i)
  elif low_r <= ranges[i-1][0] and high_r >= ranges[i-1][1]:
    ranges[i-1][0] = low_r
    ranges[i-1][1] = high_r
    ranges.pop(i)
  elif low_r <= ranges[i-1][0] and high_r >= ranges[i-1][0]:
    ranges[i-1][0] = low_r
    ranges.pop(i)
  elif high_r >= ranges[i-1][1] and low_r <= ranges[i-1][1]:
    ranges[i-1][1] = high_r
    ranges.pop(i)
  else:
    i += 1

max_continuous = ranges[0][1] - ranges[0][0]
for i in range(1, len(ranges)):
  diff = ranges[i][1] - ranges[i][0]
  if diff > max_continuous:
    max_continuous = diff

max_idle = 0
if len(ranges) > 1:
  max_idle = ranges[1][0] - ranges[0][1]
  for i in range(2, len(ranges)):
    diff = ranges[i][0] - ranges[i-1][1]
    if diff > max_idle:
      max_idle = diff

with open("milk2.out", "w") as fileOut:
  out = str(max_continuous) + " " + str(max_idle) + "\n"
  fileOut.write(out)
  print(out)

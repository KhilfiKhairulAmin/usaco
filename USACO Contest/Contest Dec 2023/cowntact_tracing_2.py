input()
cows = input()


def cowntact_tracking(cows: list):

  if cows.count('1') == len(cows):
    return 1
  elif cows.count('0') == len(cows):
    return 0
  
  n_end = 0
  count_end = []
  count = 0
  max_nights_1 = -1
  start, end = 0, len(cows) - 1
  for i in range(len(cows)):
    if cows[i] == '1':
      max_nights_1 += 1
      start += 1
      count += 1
    else:
      if count > 0:
        count_end.append(count)
      break
  
  count = 0
  max_nights_2 = -1
  for i in range(len(cows) - 1, 0, -1):
    if cows[i] == '1':
      max_nights_2 += 1
      end -= 1
      count += 1
    else:
      if count > 0:
        count_end.append(count)
      break

  min_nights_end = -1
  if max_nights_1 != -1 and max_nights_2 != -1:
    min_nights_end = max_nights_1 if max_nights_1 < max_nights_2 else max_nights_2
    n_end += 2
  elif max_nights_1 != -1:
    min_nights_end = max_nights_1
    n_end += 1
  elif max_nights_2 != -1:
    min_nights_end = max_nights_2
    n_end += 1

  count_1s = []
  count = 0
  for i in range(start+1, end):
    if cows[i] == '1':
      count += 1
    else:
      if count != 0:
        count_1s.append(count)
      count = 0
  if count != 0:
    count_1s.append(count)

  # print(count_1s)
  min_nights = len(cows)
  for j in range(len(count_1s)):
    lo = int((count_1s[j] - 1) / 2)
    if lo < min_nights:
      min_nights = lo
  
  if min_nights_end != -1:
    min_nights = min_nights if min_nights < min_nights_end else min_nights_end
  # print(min_nights)
  if min_nights == 0:
    return cows.count('1')
  
  for k in range(min_nights, 0, -1):
    if k == 1:
      for i in range(len(count_1s)):
        if count_1s[i] > 4:
          count_1s[i] = int((count_1s[i] - 1) / 2)
        else:
          count_1s[i] = int(count_1s[i] / 2)
      continue
    for i in range(len(count_1s)):
      count_1s[i] -= 1

  # print(n_end, min_nights)

  for m in range(min_nights, 0, -1):
    # print(count_end)
    if m == 1:
      for i in range(len(count_end)):
        if count_end[i] > 4:
          count_end[i] = int((count_end[i] - 1) / 2)
        else:
          count_end[i] = int(count_end[i] / 2)
      continue
    for i in range(len(count_end)):
      count_end[i] -= 1

  print(min_nights)

  # print(count_end)
  # print(count_1s, count_end)
  count = sum(count_1s) + sum(count_end)
  return count



print(cowntact_tracking(cows))

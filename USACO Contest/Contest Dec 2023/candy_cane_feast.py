N, M = (int(x) for x in input().split(" "))
n_cows = [int(x) for x in input().split(" ")]
m_canes = [int(x) for x in input().split(" ")]

cur_m, cur_n = 0, 0
lo = 0

while cur_m != M:
  hi = m_canes[cur_m]

  if n_cows[cur_n] >= hi:
    n_cows[cur_n] += hi - lo
    cur_n = N
  elif n_cows[cur_n] > lo:
    temp = n_cows[cur_n]
    n_cows[cur_n] += n_cows[cur_n] - lo
    lo = temp
    cur_n += 1
  else:
    cur_n += 1
  
  if cur_n == N:
    cur_n = 0
    cur_m += 1
    lo = 0

  
for cow in n_cows:
  print(cow)

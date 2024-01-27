"""
ID: khilfik1
LANG: PYTHON3
PROG: beads
"""

necklace = ""
with open("beads.in") as fileIn:
  len_necklace = int(next(fileIn).replace("\n", ""))
  necklace = next(fileIn)[:-1]
  necklace *= 2


def max_beads(necklace: str):

  # All are same
  if necklace.count(necklace[0]) == len(necklace):
    return len_necklace
  
  """
  Preprocess necklace
  """
  # Starting w
  if necklace[0] == "w":
    w = 0
    while necklace[w] == "w":
      w += 1
    necklace = necklace[w] * w + necklace[w:]

  # Ending w
  if necklace[-1] == "w":
    w = -1
    while necklace[w] == "w":
      w -= 1
    necklace = necklace[0:w] + necklace[w] * -w

  # Middle w
  for i in range(len(necklace)):
    if necklace[i] == "w":
      temp = i
      while necklace[i] == "w":
        i += 1
      if necklace[temp-1] == necklace[i]:
        necklace = necklace[:temp] + necklace[i] * (i - temp) + necklace[i:]

  order_b = [necklace[0]]
  count_i = [0]
  for b in necklace:
    if b == order_b[-1]:
      count_i[-1] += 1
    else:
      order_b.append(b)
      count_i.append(1)

  # Determine the length  of each possible substrands
  sub_strands = [0]
  i, strand_len = 0, 0
  j = -1
  while i != len(order_b):
    if order_b[i] == "w":
      sub_strands[-1] += count_i[i]
      i += 1

    if strand_len == 2:
      i = j
      j -= 1
      strand_len = 0
      sub_strands.append(0)
    elif order_b[i] != "w":
        sub_strands[-1] += count_i[i]
        strand_len += 1
        i += 1
        j += 1

  max_substrand = max(sub_strands)
  return max_substrand if max_substrand <= len_necklace else len_necklace
  

with open("beads.out", "w") as fileOut:
  out = str(max_beads(necklace)) + "\n"
  fileOut.write(out)
  print(out)

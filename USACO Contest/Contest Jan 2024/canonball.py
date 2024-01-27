class Pad:
  v = 1
  q = 0
  broke = False


n, s = [int(x) for x in input().split(" ")]

pads = []
for _ in range(n):
  q, v = [int(x) for x in input().split(" ")]
  pad = Pad()
  pad.v = v
  pad.q = q
  pads.append(pad)

broken = 0
k = 1
direction = 1
s -= 1
n -= 1
infi_tracker = []
while s >= 0 and s <= n:
  if pads[s].q == 0:
    k += pads[s].v
    direction *= -1

    if pads[s].v == 0:
      if pads[s] in infi_tracker:
        break
      else:
        infi_tracker.append(pads[s])
    else:
      infi_tracker.clear()
  else:
    if not pads[s].broke and k >= pads[s].v:
      pads[s].broke = True
      broken += 1
      infi_tracker.clear()
  s += k * direction

print(broken)

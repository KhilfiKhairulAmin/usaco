"""
ID: khilfik1
LANG: PYTHON3
TASK: gift1
"""

people = {}

def give(giver: str, amount: int, receivers: list[str]):
  leftover = amount % len(receivers)
  people[giver] -= amount
  people[giver] += leftover

  receive = int(amount / len(receivers))
  for receiver in receivers:
    people[receiver] += receive


with open("gift1.in") as fileIn:
  np = int(next(fileIn)[:-1])
  for i in range(np):
    people[next(fileIn)] = 0
  
  for line in fileIn:
    giver = line

    amount, ng = next(fileIn).split(" ")
    amount = int(amount)
    ng = int(ng)
    if ng == 0:
      continue

    receivers = []
    for i in range(ng):
      receivers.append(next(fileIn))
    
    give(giver, amount, receivers)
    
with open("gift1.out", "w") as fileOut:
  for k in people.keys():
    out = k[:-1] + " " + str(people[k]) + "\n"
    fileOut.write(out)
    print(out, end="")

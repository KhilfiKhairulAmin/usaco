"""
ID: khilfik1
LANG: PYTHON3
PROG: ride
"""
output = ""
char_map = {
  "\n": 1,
  "A": 1,
  "B": 2,
  "C": 3,
  "D": 4,
  "E": 5,
  "F": 6,
  "G": 7,
  "H": 8,
  "I": 9,
  "J": 10,
  "K": 11,
  "L": 12,
  "M": 13,
  "N": 14,
  "O": 15,
  "P": 16,
  "Q": 17,
  "R": 18,
  "S": 19,
  "T": 20,
  "U": 21,
  "V": 22,
  "W": 23,
  "X": 24,
  "Y": 25,
  "Z": 26,
}

def nameProduct(name):
  product = 1
  for c in name:
    product *= char_map[c]
  return product

def compareCometAndGroup(comet_name, group_name):
  return nameProduct(comet_name) % 47 == nameProduct(group_name) % 47

with open("ride.in", "r") as fileIn:
  comet = next(fileIn)
  group = next(fileIn)
  output = "GO" if compareCometAndGroup(comet, group) else "STAY"
  output += "\n"

with open("ride.out", "w") as fileOut:
  fileOut.write(output)
  print(output)

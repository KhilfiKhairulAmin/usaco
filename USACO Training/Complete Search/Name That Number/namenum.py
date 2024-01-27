"""
ID: khilfik1
LANG: PYTHON3
TASK: namenum
"""
num_map = {
  "A": "2", "B": "2", "C": "2",
  "D": "3", "E": '3', "F": "3",
  "G": "4", "H": "4", "I": "4",
  "J": "5", "K": "5", "L": "5",
  "M": "6", "N": "6", "O": "6",
  "P": "7", "R": "7", "S": "7",
  "T": "8", "U": "8", "V": "8",
  "W": "9", "X": "9", "Y": "9",
  "Q": "0", "Z": "0", "\n": ""
}


def name_to_serial(name):
  serial = ""
  for c in name:
    if num_map[c] == "0":
      return ""
    serial += num_map[c]
  return serial


target_serial_num = ""
with open("namenum.in") as fileIn:
  target_serial_num = next(fileIn)[:-1]


out = ""
with open("dict.txt") as fileIn:
  for name in fileIn:
    serial_num = name_to_serial(name)
    if serial_num == target_serial_num:
      out += name


out = out if out else "NONE\n"
with open("namenum.out", "w") as fileOut:
  fileOut.write(out)
  print(out)

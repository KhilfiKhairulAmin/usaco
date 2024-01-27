"""
ID: khilfik1
LANG: PYTHON3
TASK: transform
"""
obj = []
img = []
with open("transform.in") as fileIn:
  N = int(next(fileIn)[:-1])
  for i in range(N):
    obj.append([x for x in next(fileIn)[:-1]])
  for i in range(N):
    img.append([x for x in next(fileIn)[:-1]])


def compare(obj, img):
  for i in range(N):
    for j in range(N):
      if obj[i][j] != img[i][j]:
        return False
  return True


def print_img(img):
  for i in range(len(img)):
    print(img[i])
  print()


def rotate_90_clockwise(obj: list[list]):
  n_rot = N - 1
  right, left = 0, n_rot
  temp_img = []
  for _ in range(n_rot, 0, -2):
    temp_img = obj[right][right:left]
    for j in range(right, left):
      temp = obj[j][left]
      obj[j][left] = temp_img[j - right]
      temp_img[j - right] = temp
    for k in range(left, right, -1):
      temp = obj[left][k]
      obj[left][k] = temp_img[-k + left]
      temp_img[-k + left] = temp
    for n in range(left, right, -1):
      temp = obj[n][right]
      obj[n][right] = temp_img[-n + left]
      temp_img[-n + left] = temp
    for o in range(right, left):
      obj[right][o] = temp_img[o - right]
    right += 1
    left -= 1

  return obj


def h_reflection(obj: list[list]):
  r, l = 0, N - 1
  for _ in range(0, int(N / 2)):
    for i in range(N):
      temp = obj[i][r]
      obj[i][r] = obj[i][l]
      obj[i][l] = temp
    r += 1
    l -= 1
  
  return obj


def transformations(obj, img):
  
  if compare(rotate_90_clockwise(obj), img):
    return 1

  if compare(rotate_90_clockwise(obj), img):
    return 2

  if compare(rotate_90_clockwise(obj), img):
    return 3
  
  rotate_90_clockwise(obj)
  if compare(h_reflection(obj), img):
    return 4
  
  if compare(rotate_90_clockwise(obj), img) or compare(rotate_90_clockwise(obj), img) or compare(rotate_90_clockwise(obj), img):
    return 5

  rotate_90_clockwise(obj)
  h_reflection(obj)
  if compare(obj, img):
    return 6
  
  return 7


with open("transform.out", "w") as fileOut:
  out = str(transformations(obj, img)) + "\n"
  fileOut.write(out)
  print(out)

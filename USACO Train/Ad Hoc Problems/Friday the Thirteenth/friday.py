"""
ID: khilfik1
LANG: PYTHON3
PROG: friday
"""

# Day Mapping
#   0: "Saturday"
#   1: "Sunday"
#   2: "Monday"
#   3: "Tuesday"
#   4: "Wednesday"
#   5: "Thursday"
#   6: "Friday"

count_days = {
  0: 0,
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
}

N = 0
with open("friday.in") as fileIn:
  N = int(next(fileIn)[:-1])

n_month = N * 12
cur_day = 2 # Start at 1 Jan, 1900 (Monday)

for y in range(1900, 1900+N):
  # Calculate for each month in one year
  # Jan
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 31) % 7

  # Feb
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  feb_days = 28
  if y % 4 == 0:
    if y % 100 == 0: # Check for century years
      if y % 400 == 0:
        feb_days = 29
    else:
      feb_days = 29
  cur_day = (temp + feb_days) % 7

  # Mar
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 31) % 7

  # Apr
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 30) % 7

  # May
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 31) % 7

  # Jun
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 30) % 7

  # Jul
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 31) % 7

  # Aug
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 31) % 7

  # Sep
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 30) % 7

  # Oct
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 31) % 7

  # Nov
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 30) % 7

  # Dec
  temp = cur_day
  cur_day += 12 # To go to 13th from the 1st, increment by 12
  count_days[cur_day%7] += 1
  cur_day = (temp + 31) % 7

with open("friday.out", "w") as fileOut:
  out = " ".join([str(v) for v in count_days.values()]) + "\n"
  fileOut.write(out)
  print(out)

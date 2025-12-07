import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/1.txt") as f:
      return f.readlines()

def part1():
   lines = get_lines()
   curr = 50
   res = 0

   for line in lines:
      dir = line[0]
      count = int(line[1:])

      if dir == "L":
         curr -= count
      else:
         curr += count

      if curr % 100 == 0:
         res += 1

   return res

def part2():
   lines = get_lines()
   curr = 50
   res = 0

   for line in lines:
      dir = line[0]
      count = int(line[1:])

      if dir == "L":
         # If prev value was 0, then add 100 to stop off-by-1
         if curr == 0:
            curr += 100
         curr -= count

         while curr < 0:
            curr += 100
            res += 1

         # Due to 0 handling above, we need to give extra point when we hit zero
         if curr == 0:
            res += 1
      elif dir == "R":
         curr += count
         while curr >= 100:
            curr -= 100
            res += 1

   return res
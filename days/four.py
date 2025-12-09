import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/4.txt") as f:
      return f.readlines()

def part1():
   lines = get_lines()
   rolls = [[x for x in line if x != "\n"] for line in lines]
   res = 0

   for i in range(len(rolls)):
      for j in range(len(rolls[i])):
         roll = rolls[i][j]
         if roll != "@":
            continue
         count = -1 # -1 to handle k==0 and l==0

         for k in range(-1, 2):
            idx = i + k
            if idx < 0 or idx >= len(rolls):
               continue
            for l in range(-1, 2):
               jdx = j + l
               if jdx < 0 or jdx >= len(rolls[idx]):
                  continue
               surrounding_roll = rolls[i+k][j+l]
               if surrounding_roll == "@":
                  count += 1

         if count < 4:
            res += 1

   return res

# Not going to generalise the code as I want to alter the map
# while iterating through for perf gain
def part2():
   lines = get_lines()
   rolls = [[x for x in line if x != "\n"] for line in lines]
   prev_res = -1
   res = 0

   while res != prev_res:
      prev_res = res

      # This is just copied from part one
      for i in range(len(rolls)):
         for j in range(len(rolls[i])):
            roll = rolls[i][j]
            if roll != "@":
               continue
            count = -1 # -1 to handle k==0 and l==0

            for k in range(-1, 2):
               idx = i + k
               if idx < 0 or idx >= len(rolls):
                  continue
               for l in range(-1, 2):
                  jdx = j + l
                  if jdx < 0 or jdx >= len(rolls[idx]):
                     continue
                  surrounding_roll = rolls[i+k][j+l]
                  if surrounding_roll == "@":
                     count += 1

            if count < 4:
               res += 1
               rolls[i][j] = "."

   return res
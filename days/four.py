import logging
from itertools import product
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/4.txt") as f:
      return f.readlines()

def get_surrounding_count(i: int, j: int, rolls: List[List[str]]):
   count = -1 # -1 to handle k==0 and l==0

   surrounding = product([0,-1,1], [0,-1,1])
   for k, l in surrounding:
      idx = i + k
      if idx < 0 or idx >= len(rolls):
         continue
      jdx = j + l
      if jdx < 0 or jdx >= len(rolls[idx]):
         continue
      surrounding_roll = rolls[idx][jdx]
      if surrounding_roll == "@":
         count += 1

   return count

def part1():
   lines = get_lines()
   rolls = [[x for x in line if x != "\n"] for line in lines]
   res = 0

   for i in range(len(rolls)):
      for j in range(len(rolls[i])):
         roll = rolls[i][j]
         if roll != "@":
            continue
         count = get_surrounding_count(i, j, rolls)

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
            count = get_surrounding_count(i, j, rolls)

            if count < 4:
               res += 1
               rolls[i][j] = "."

   return res
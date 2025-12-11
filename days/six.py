import logging
from math import prod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/6.txt") as f:
      return [line.strip("\n") for line in f.readlines()]

def transpose(matrix: list[list[str]]) -> list[list[str]]:
   return list(map(list, zip(*matrix)))

def part1():
   lines = get_lines()
   matrix = [[item for item in line.split(" ") if item.strip() != ""] for line in lines]
   equations = transpose(matrix)

   res = 0
   for *nums, op in equations:
      if op == "+":
         res += sum(map(int, nums))
      else:
         res += prod(map(int, nums))

   return res


def part2():
   lines = get_lines()
   line_len = max(len(line) for line in lines)

   # Need all this logic to appropriately pad zeros before and after
   # While maintaining columns
   i = 0
   equations: list[list[str]] = [[]]
   while i < line_len:
      # Need this temp logic to check if every element is " "
      temp = set()

      for line in lines:
         temp.add(line[i])

      if len(temp) == 1 and " " in temp:
         i += 1
         equations.append([])
         continue

      # Main logic for getting column values
      res = [""] * len(lines)

      for j, line in enumerate(lines):
         res[j] += line[i] if (line[i] != " ") else ""

      *nums, op = res
      if op != "":
         equations[-1].append(op)
      equations[-1].append("".join(nums))
      i += 1

   res = 0
   for op, *nums in equations:
      if op == "+":
         res += sum(map(int, nums))
      else:
         res += prod(map(int, nums))

   return res
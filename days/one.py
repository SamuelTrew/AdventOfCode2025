import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("../input/1.txt") as f:
      return f.readlines()

def part1():
   lines = get_lines()
   curr = 50

   for line in lines:
      dir = line[0]
      count = int(line[1:])
      print(dir, count)


   return 0

def part2():
   lines = get_lines()

   return 0
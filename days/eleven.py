import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/11.txt") as f:
      return [line.strip("\n") for line in f.readlines()]

def part1():
   lines = get_lines()

   return 0

def part2():
   lines = get_lines()

   return 0
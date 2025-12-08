import logging
from functools import reduce

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/2.txt") as f:
      return "".join(f.readlines()).split(",")

def part1():
   lines = get_lines()
   invalid: list[int] = []

   for line in lines:
      start, end = line.split("-")
      for num in range(int(start), int(end) + 1):
         num_str = str(num)
         if len(num_str) % 2 == 1:
            continue
         fst, snd = num_str[:len(num_str)//2], num_str[len(num_str)//2:]
         if fst == snd:
            invalid.append(num)

   return sum(invalid)

def all_chunks_same(xs: str, chunk_size: int):
   chunks = [xs[i:i+chunk_size] for i in range(0, len(xs), chunk_size)]

   for i in range(1, len(chunks)):
      prev = chunks[i-1]
      curr = chunks[i]
      if prev != curr:
         return False
   return True

def part2():
   lines = get_lines()
   invalid: set[int] = set()

   for line in lines:
      start, end = line.split("-")
      for num in range(int(start), int(end) + 1):
         num_str = str(num)

         # Effectively getting all factors of len(num_str)
         for i in range(1, len(num_str)):
            # Ignore perfect divisions
            if len(num_str) % i != 0:
               continue
            if all_chunks_same(num_str, i):
               invalid.add(num)

   return sum(invalid)
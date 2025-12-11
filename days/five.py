import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/5.txt") as f:
      return [line.strip("\n") for line in f.readlines()]

def part1():
   lines = get_lines()
   idx = lines.index("")
   ranges, available = lines[:idx], list(map(int, lines[idx+1:]))
   pairs = [(int(a), int(b)) for x in ranges for a, b in [x.split("-")]]

   count = 0

   for item in available:
      for start, end in pairs:
         if start <= item <= end:
            count += 1
            break

   return count

# Could iterate over everything and chuck into set but that's boring
def part2():
   lines = get_lines()
   idx = lines.index("")
   ranges = lines[:idx]
   pairs = sorted([(int(a), int(b)) for x in ranges for a, b in [x.split("-")]])

   count = 0
   last_end = -1

   for start, end in pairs:
      if last_end >= end:
         continue

      if last_end >= start:
         count += end - last_end
      else:
         count += end - start + 1

      last_end = end

   return count
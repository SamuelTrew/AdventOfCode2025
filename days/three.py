import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_lines():
   with open("input/3.txt") as f:
      return f.readlines()

def part1():
   lines = get_lines()
   batteries = [[int(x) for x in line if x.isnumeric()] for line in lines]
   res = 0

   for line in batteries:
      fst, snd = -1, -1
      p = 0

      while p < len(line) - 1:
         battery = line[p]
         next_battery = line[p+1]

         if battery > fst:
            fst = battery
            snd = next_battery
         elif battery > snd:
            snd = battery

         p += 1

      # Handle last item in list
      if line[p] > snd:
         snd = line[p]

      res += (fst * 10) + snd

   return res

def part2():
   lines = get_lines()
   batteries = [list(reversed([int(x) for x in line if x.isnumeric()])) for line in lines]
   res = 0

   for line in batteries:
      slice = list(reversed(line[:12]))

      for p in range(12, len(line)):
         battery = line[p]

         for i in range(12):
            curr = slice[i]
            if battery > curr:
               slice[i] = battery
               battery = curr
            elif battery == curr:
               continue
            else:
               break

      res += int("".join(map(str, slice)))

   return res

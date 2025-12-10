from days.five import part1, part2
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    t1 = time.perf_counter()
    res1 = part1()
    t2 = time.perf_counter()
    logger.info(f"Part 1 took {round(t2-t1, 4)} seconds. Result = {res1}")

    t3 = time.perf_counter()
    res2 = part2()
    t4 = time.perf_counter()
    logger.info(f"Part 2 took {round(t4-t3, 4)} seconds. Result = {res2}")


if __name__ == "__main__":
    main()

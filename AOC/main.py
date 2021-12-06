from AOC.Day1 import sonar_sweep
from AOC.Day2 import dive
from AOC.Day3 import binary_diagnostic
from AOC.Day4 import giant_squid
from AOC.Day5 import hydrothermal_venture

message_format = "Day {}: answer for puzzle 1 is {} and for puzzle 2 is {}"
print("Advent of Code 2021")

# Day 1
result1, result2 = sonar_sweep.sonar_sweep()
print(message_format.format(1, result1, result2))

# Day 2
result1, result2 = dive.dive()
print(message_format.format(2, result1, result2))

# Day 3
# binary_diagnostic.binary_diagnostic1()
# binary_diagnostic.binary_diagnostic2()
# print(binary_diagnostic.binary_diagnostic())

# Day 4
result1, result2 = giant_squid.giant_squid()
print(message_format.format(4, result1, result2))

# Day 5
result1, result2 = hydrothermal_venture.hydrothermal_venture()
print(message_format.format(5, result1, result2))

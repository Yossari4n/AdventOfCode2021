from pyDvent.Year2021 import sonar_sweep, dive, binary_diagnostic, giant_squid, hydrothermal_venture, lanternfish, \
    the_treachery_of_whales, seven_segment_search, smoke_basin, syntax_scoring, dumbo_octopus, passage_pathing, \
    transparent_origami, extended_polymerization, chiton, packet_decoder, trick_shot, snailfish, beacon_scanner, \
    trench_map, dirac_dice, reactor_reboot, amphipod, arithmetic_logic_unit, sea_cucumber
from pyDvent.Year2022 import calorie_counting, rock_paper_scissors, rucksack_reorganization, camp_cleanup, \
    supply_stacks, tuning_trouble
from enum import Enum, IntEnum
import time


class Years(Enum):
    Year2015 = 1,
    Year2016 = 2,
    Year2017 = 3,
    Year2018 = 4,
    Year2019 = 5,
    Year2020 = 6,
    Year2021 = 7,
    Year2022 = 8


class Days(IntEnum):
    Day1 = 1,
    Day2 = 2,
    Day3 = 3,
    Day4 = 4,
    Day5 = 5,
    Day6 = 6,
    Day7 = 7,
    Day8 = 8,
    Day9 = 9,
    Day10 = 10,
    Day11 = 11,
    Day12 = 12,
    Day13 = 13,
    Day14 = 14,
    Day15 = 15,
    Day16 = 16,
    Day17 = 17,
    Day18 = 18,
    Day19 = 19,
    Day20 = 20,
    Day21 = 21,
    Day22 = 22,
    Day23 = 23,
    Day24 = 24,
    Day25 = 25


solutions = {
    Years.Year2021: {
        Days.Day1: sonar_sweep.sonar_sweep,
        Days.Day2: dive.dive,
        Days.Day3: binary_diagnostic.binary_diagnostic,
        Days.Day4: giant_squid.giant_squid,
        Days.Day5: hydrothermal_venture.hydrothermal_venture,
        Days.Day6: lanternfish.lanternfish,
        Days.Day7: the_treachery_of_whales.the_treachery_of_whales,
        Days.Day8: seven_segment_search.seven_segment_search,
        Days.Day9: smoke_basin.smoke_basin,
        Days.Day10: syntax_scoring.syntax_scoring,
        Days.Day11: dumbo_octopus.dumbo_octopus,
        Days.Day12: passage_pathing.passage_pathing,
        Days.Day13: transparent_origami.transparent_origami,
        Days.Day14: extended_polymerization.extended_polymerization,
        Days.Day15: chiton.chiton,
        Days.Day16: packet_decoder.packet_decoder,
        Days.Day17: trick_shot.trick_shot,
        Days.Day18: snailfish.snailfish,
        Days.Day19: beacon_scanner.beacon_scanner,
        Days.Day20: trench_map.trench_map,
        Days.Day21: dirac_dice.dirac_dice,
        Days.Day22: reactor_reboot.reactor_reboot,
        Days.Day23: amphipod.amphipod,
        Days.Day24: arithmetic_logic_unit.arithmetic_logic_unit,
        Days.Day25: sea_cucumber.sea_cucumber
    },
    Years.Year2022: {
        Days.Day1: calorie_counting.calorie_counting,
        Days.Day2: rock_paper_scissors.rock_paper_scissors,
        Days.Day3: rucksack_reorganization.rucksack_reorganization,
        Days.Day4: camp_cleanup.camp_cleanup,
        Days.Day5: supply_stacks.supply_stacks,
        Days.Day6: tuning_trouble.tuning_trouble,
    }
}


def print_solution(year, day, file_path):
    start = time.time()
    result1, result2 = solutions[year][day](file_path)
    end = time.time()
    message_format = "Solved {0} {1} in {2:.5f}s, results are\nPart 1: {3}\nPart 2: {4}"
    print(message_format.format(year.name, day.name, end - start, result1, result2))


print("Advent of Code")
print_solution(Years.Year2022, Days.Day6, 'input/Year2022/Day6.txt')

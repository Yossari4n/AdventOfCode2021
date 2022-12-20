from pyDvent.Year2021 import sonar_sweep, dive, binary_diagnostic, giant_squid, hydrothermal_venture, lanternfish, \
    the_treachery_of_whales, seven_segment_search, smoke_basin, syntax_scoring, dumbo_octopus, passage_pathing, \
    transparent_origami, extended_polymerization, chiton, packet_decoder, trick_shot, snailfish, beacon_scanner, \
    trench_map, dirac_dice, reactor_reboot, amphipod, arithmetic_logic_unit, sea_cucumber
from pyDvent.Year2022 import calorie_counting, rock_paper_scissors, rucksack_reorganization, camp_cleanup, \
    supply_stacks, tuning_trouble, no_space_left_on_device, treetop_tree_house, rope_bridge, cathorode_tube, \
    monkey_in_the_middle, hill_climbing_algorithm
import pytest


@pytest.mark.parametrize("solution", [
    [sonar_sweep.sonar_sweep, '../test_input/Year2021/Day1_input.txt', '../test_input/Year2021/Day1_output1.txt', '../test_input/Year2021/Day1_output2.txt'],
    [dive.dive, '../test_input/Year2021/Day2_input.txt', '../test_input/Year2021/Day2_output1.txt', '../test_input/Year2021/Day2_output2.txt'],
    [binary_diagnostic.binary_diagnostic, '../test_input/Year2021/Day3_input.txt', '../test_input/Year2021/Day3_output1.txt', '../test_input/Year2021/Day3_output2.txt'],
    [giant_squid.giant_squid, '../test_input/Year2021/Day4_input.txt', '../test_input/Year2021/Day4_output1.txt', '../test_input/Year2021/Day4_output2.txt'],
    [hydrothermal_venture.hydrothermal_venture, '../test_input/Year2021/Day5_input.txt', '../test_input/Year2021/Day5_output1.txt', '../test_input/Year2021/Day5_output2.txt'],
    [lanternfish.lanternfish, '../test_input/Year2021/Day6_input.txt', '../test_input/Year2021/Day6_output1.txt', '../test_input/Year2021/Day6_output2.txt'],
    [the_treachery_of_whales.the_treachery_of_whales, '../test_input/Year2021/Day7_input.txt', '../test_input/Year2021/Day7_output1.txt', '../test_input/Year2021/Day7_output2.txt'],
    [seven_segment_search.seven_segment_search, '../test_input/Year2021/Day8_input.txt', '../test_input/Year2021/Day8_output1.txt', '../test_input/Year2021/Day8_output2.txt'],
    [smoke_basin.smoke_basin, '../test_input/Year2021/Day9_input.txt', '../test_input/Year2021/Day9_output1.txt', '../test_input/Year2021/Day9_output2.txt'],
    [syntax_scoring.syntax_scoring, '../test_input/Year2021/Day10_input.txt', '../test_input/Year2021/Day10_output1.txt', '../test_input/Year2021/Day10_output2.txt'],
    [dumbo_octopus.dumbo_octopus, '../test_input/Year2021/Day11_input.txt', '../test_input/Year2021/Day11_output1.txt', '../test_input/Year2021/Day11_output2.txt'],
    [passage_pathing.passage_pathing, '../test_input/Year2021/Day12_input.txt', '../test_input/Year2021/Day12_output1.txt', '../test_input/Year2021/Day12_output2.txt'],
    [transparent_origami.transparent_origami, '../test_input/Year2021/Day13_input.txt', '../test_input/Year2021/Day13_output1.txt', '../test_input/Year2021/Day13_output2.txt'],
    [extended_polymerization.extended_polymerization, '../test_input/Year2021/Day14_input.txt', '../test_input/Year2021/Day14_output1.txt', '../test_input/Year2021/Day14_output2.txt'],
    [chiton.chiton, '../test_input/Year2021/Day15_input.txt', '../test_input/Year2021/Day15_output1.txt', '../test_input/Year2021/Day15_output2.txt'],
    [packet_decoder.packet_decoder, '../test_input/Year2021/Day16_input.txt', '../test_input/Year2021/Day16_output1.txt', '../test_input/Year2021/Day16_output2.txt'],
    [trick_shot.trick_shot, '../test_input/Year2021/Day17_input.txt', '../test_input/Year2021/Day17_output1.txt', '../test_input/Year2021/Day17_output2.txt'],
    [snailfish.snailfish, '../test_input/Year2021/Day18_input.txt', '../test_input/Year2021/Day18_output1.txt', '../test_input/Year2021/Day18_output2.txt'],
    [beacon_scanner.beacon_scanner, '../test_input/Year2021/Day19_input.txt', '../test_input/Year2021/Day19_output1.txt', '../test_input/Year2021/Day19_output2.txt'],
    [trench_map.trench_map, '../test_input/Year2021/Day20_input.txt', '../test_input/Year2021/Day20_output1.txt', '../test_input/Year2021/Day20_output2.txt'],
    [dirac_dice.dirac_dice, '../test_input/Year2021/Day21_input.txt', '../test_input/Year2021/Day21_output1.txt', '../test_input/Year2021/Day21_output2.txt'],
    [reactor_reboot.reactor_reboot, '../test_input/Year2021/Day22_input.txt', '../test_input/Year2021/Day22_output1.txt', '../test_input/Year2021/Day22_output2.txt'],
    [amphipod.amphipod, '../test_input/Year2021/Day23_input.txt', '../test_input/Year2021/Day23_output1.txt', '../test_input/Year2021/Day23_output2.txt'],
    [arithmetic_logic_unit.arithmetic_logic_unit, '../test_input/Year2021/Day24_input.txt', '../test_input/Year2021/Day24_output1.txt', '../test_input/Year2021/Day24_output2.txt'],
    [sea_cucumber.sea_cucumber, '../test_input/Year2021/Day25_input.txt', '../test_input/Year2021/Day25_output1.txt', '../test_input/Year2021/Day25_output2.txt'],

    [calorie_counting.calorie_counting, '../test_input/Year2022/Day1_input.txt', '../test_input/Year2022/Day1_output1.txt', '../test_input/Year2022/Day1_output2.txt'],
    [rock_paper_scissors.rock_paper_scissors, '../test_input/Year2022/Day2_input.txt', '../test_input/Year2022/Day2_output1.txt', '../test_input/Year2022/Day2_output2.txt'],
    [rucksack_reorganization.rucksack_reorganization, '../test_input/Year2022/Day3_input.txt', '../test_input/Year2022/Day3_output1.txt', '../test_input/Year2022/Day3_output2.txt'],
    [camp_cleanup.camp_cleanup, '../test_input/Year2022/Day4_input.txt', '../test_input/Year2022/Day4_output1.txt', '../test_input/Year2022/Day4_output2.txt'],
    [supply_stacks.supply_stacks, '../test_input/Year2022/Day5_input.txt', '../test_input/Year2022/Day5_output1.txt', '../test_input/Year2022/Day5_output2.txt'],
    [tuning_trouble.tuning_trouble, '../test_input/Year2022/Day6_input.txt', '../test_input/Year2022/Day6_output1.txt', '../test_input/Year2022/Day6_output2.txt'],
    [no_space_left_on_device.no_space_left_on_device, '../test_input/Year2022/Day7_input.txt', '../test_input/Year2022/Day7_output1.txt', '../test_input/Year2022/Day7_output2.txt'],
    [treetop_tree_house.treetop_tree_house, '../test_input/Year2022/Day8_input.txt', '../test_input/Year2022/Day8_output1.txt', '../test_input/Year2022/Day8_output2.txt'],
    [rope_bridge.rope_bridge, '../test_input/Year2022/Day9_input.txt', '../test_input/Year2022/Day9_output1.txt', '../test_input/Year2022/Day9_output2.txt'],
    [cathorode_tube.cathorode_tube, '../test_input/Year2022/Day10_input.txt', '../test_input/Year2022/Day10_output1.txt', '../test_input/Year2022/Day10_output2.txt'],
    [monkey_in_the_middle.monkey_in_the_middle, '../test_input/Year2022/Day11_input.txt', '../test_input/Year2022/Day11_output1.txt', '../test_input/Year2022/Day11_output2.txt'],
    [hill_climbing_algorithm.hill_climbing_algorithm, '../test_input/Year2022/Day12_input.txt', '../test_input/Year2022/Day12_output1.txt', '../test_input/Year2022/Day12_output2.txt'],
])
def test_solutions(solution):
    func = solution[0]
    input_path = solution[1]
    output_path1, output_path2 = solution[2], solution[3]
    with open(output_path1, 'r') as output1, open(output_path2, 'r') as output2:
        output1 = output1.read()
        output2 = output2.read()

    result1, result2 = func(input_path)
    assert str(result1) == output1 and str(result2) == output2

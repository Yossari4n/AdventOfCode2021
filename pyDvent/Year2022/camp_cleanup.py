import re


def camp_cleanup(file_path):
    with open(file_path, 'r') as input_file:
        overlaps = 0
        partial_overlaps = 0
        for pairs in input_file:
            ranges = list(map(int, re.split('[-|,]', pairs)))
            if ranges[0] >= ranges[2] and ranges[1] <= ranges[3] \
                    or ranges[2] >= ranges[0] and ranges[3] <= ranges[1]:
                overlaps += 1
            if ranges[2] <= ranges[0] <= ranges[3] or ranges[2] <= ranges[1] <= ranges[3]\
                    or ranges[0] <= ranges[2] <= ranges[1] or ranges[0] <= ranges[3] <= ranges[1]:
                partial_overlaps += 1

    return overlaps, partial_overlaps

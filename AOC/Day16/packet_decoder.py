import math


def packet_decoder():
    with open('Day16/input.txt') as file:
        message = file.read().replace('\n', '')
        _, result, versions_sum = process_packet(decode_message(message))
        return versions_sum, result


def decode_message(message):
    coding = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    result_bits = ''
    for number in message:
        result_bits += coding[number]
    return result_bits


def process_literal_value_packet(packet):
    number = ''

    last_number = False
    while not last_number:
        last_number = packet[0] == '0'
        number += packet[1:5]
        packet = packet[5:]

    return packet, int(number, 2)


def calculate_expression(id_type, numbers):
    operators = {
        0: sum,
        1: math.prod,
        2: min,
        3: max,
        5: lambda nums: nums[0] > nums[1],
        6: lambda nums: nums[0] < nums[1],
        7: lambda nums: nums[0] == nums[1]
    }

    return operators[id_type](numbers)


def process_packet(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)

    if type_id == 4:
        packet, number = process_literal_value_packet(packet[6:])
        return packet, number, version
    else:
        versions_sum = version
        numbers = []

        length_type_id = int(packet[6:7], 2)
        if length_type_id == 0:
            total_length_in_bits = int(packet[7:22], 2)
            packet_to_process = packet[22:]
            packet_length = len(packet_to_process)
            while True:
                packet_to_process, number, returned_version = process_packet(packet_to_process)
                numbers.append(number)
                versions_sum += returned_version

                if packet_length - len(packet_to_process) == total_length_in_bits:
                    packet = packet_to_process
                    break
        else:
            number_of_sub_packets = int(packet[7:18], 2)
            packet = packet[18:]
            for _ in range(number_of_sub_packets):
                packet, number, returned_version = process_packet(packet)
                numbers.append(number)
                versions_sum += returned_version

        return packet, calculate_expression(type_id, numbers), versions_sum

def tuning_trouble(input_path):
    def find_marker(message, marker_size):
        for i in range(len(message) - marker_size + 1):
            if len(set(seq[i: i + marker_size])) == marker_size:
                return i + marker_size

    with open(input_path, 'r') as input_file:
        seq = input_file.read()
        return find_marker(seq, 4), find_marker(seq, 14)

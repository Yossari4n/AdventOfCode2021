class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.content = dict()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def no_space_left_on_device(input_path):
    with open(input_path, 'r') as input_file:
        commands = input_file.readlines()
        home = Directory('/')
        home.content['..'] = home

        curr = home
        for command in commands[1:]:
            command.replace('\n', '')
            command_parsed = command.split()
            if command_parsed[0] == '$':
                func = command_parsed[1]
                arg = command_parsed[2] if len(command_parsed) > 2 else ""
                if func == 'cd':
                    curr = curr.content[arg]
                elif func == 'ls':
                    pass  # ¯\_(ツ)_/¯
            else:
                if command_parsed[0] == 'dir':
                    curr.content[command_parsed[1]] = Directory(command_parsed[1])
                    curr.content[command_parsed[1]].content['..'] = curr
                elif command_parsed[0].isnumeric():
                    curr.content[command_parsed[1]] = File(command_parsed[1], int(command_parsed[0]))

        def build_dir_sizes(curr_dir):
            for k, v in curr_dir.content.items():
                if type(v) is File:
                    curr_dir.size += v.size
                elif type(v) is Directory and k != '..':
                    curr_dir.size += build_dir_sizes(v)

            return curr_dir.size
        build_dir_sizes(home)

        def build_dir_list(curr_dir, dir_list):
            dir_list.append(curr_dir)
            for k, v in curr_dir.content.items():
                if type(v) is Directory and k != '..':
                    build_dir_list(v, dir_list)
        all_dirs = []
        build_dir_list(home, all_dirs)

        result1 = sum(map(lambda d: d.size, filter(lambda d: d.size <= 100000, all_dirs)))
        required = 30000000 - (70000000 - home.size)
        result2 = min(filter(lambda d: d.size >= required, all_dirs), key=lambda d: d.size).size

        return result1, result2

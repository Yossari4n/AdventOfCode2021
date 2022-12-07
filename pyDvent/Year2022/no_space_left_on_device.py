class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.content = dict()
        self.content['..'] = parent

    def size(self):
        return sum(v.size() for _, v in list(filter(lambda p: p[0] != '..', self.content.items())))


class File:
    def __init__(self, name, size):
        self.name = name
        self.__size = size

    def size(self):
        return self.__size


def no_space_left_on_device(input_path):
    with open(input_path, 'r') as input_file:
        home = Directory('/', None)

        curr = home
        for command in input_file.readlines()[1:]:
            match command.replace('\n', '').split():
                case ['$', func, arg]:
                    curr = curr.content[arg] if func == 'cd' else curr
                case ['dir', name]:
                    curr.content[name] = Directory(name, curr)
                case [size, name] if size.isnumeric():
                    curr.content[name] = File(name, int(size))

        def flatten(curr_dir):
            ls = [(curr_dir, curr_dir.size())]
            for v in filter(lambda p: type(p[1]) is Directory and p[0] != '..', curr_dir.content.items()):
                ls.extend(flatten(v[1]))
            return ls
        all_dirs = flatten(home)

        result1 = sum(map(lambda d: d[1], filter(lambda d: d[1] <= 100000, all_dirs)))
        required = 30000000 - (70000000 - home.size())
        result2 = min(filter(lambda d: d[1] >= required, all_dirs), key=lambda d: d[1])[1]

        return result1, result2

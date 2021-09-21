import random


def generate_random_value(start, end):
    x = random.randint(start, end)
    return "example_file_{}.txt".format(x)


def create_and_fill_specified_number_of_lines(name, number_of_lines):
    # Writing to file (appending)
    with open(name, 'a') as f:
        # file_name        mode (append)
        for n in range(number_of_lines):
            f.write("Line {}\n".format(n))


def check_file_content(name, string_to_search):
    # Read the file
    elements = 0
    dikt = {string_to_search: elements}
    with open(name, 'r') as f:
        for line in f.readlines():
            if string_to_search in line.strip():
                # print(line)
                dikt[string_to_search] += 1     # elements += 1

    return "There are {} {} messages in {}".format(dikt[string_to_search],
                                                   string_to_search,
                                                   name)

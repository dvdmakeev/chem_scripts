import os
import sys

from plot import plot_intersections


# Data example:
# Molecule              Start, min  Finish, min
# TAG 15:0-15:0-15:0    17.9        18.9
# TAG 17:0-17:0-17:0    22.5        23.5
# TAG 16:0-16:0-18:1    20.2        21.2
# TAG 16:0-16:0-18:2    19          20
# TAG 16:0-16:0-18:3    18          19
# TAG 16:0-18:0-18:1    21.5        22.5
# TAG 16:0-18:0-18:2    20.4        21.4
# TAG 16:0-18:1-18:1    20          21
# TAG 16:0-18:0-18:3    19.6        20.6


def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines


def parse_data(lines):
    data = []

    for line in lines[1:]:
        line = line.strip().split(",")
        data.append({
            'molecule': line[0],
            'start': float(line[1]),
            'finish': float(line[2])
        })

    return data


# Data example:
# Molecule  Start, min  Finish, min
# A         0           5
# B         2           4
# C         3           6
# D         5           7
# Expected result:
# 0: ['A']              1
# 2: ['A', 'B']         2
# 3: ['A', 'B', 'C']    3
# 4: ['A', 'C']         2
# 5: ['C', 'D']         2
# 6: ['D']              1
# 7: []                 0


def find_intersections(data: list[dict]) -> dict[float, list[str]]:
    starts_map: dict[float, list[str]] = {}
    finishes_map: dict[float, list[str]] = {}

    for item in data:
        start = item['start']
        finish = item['finish']
        molecule = item['molecule']

        if starts_map.get(start) is None:
            starts_map[start] = []
        starts_map[start].append(molecule)

        if finishes_map.get(finish) is None:
            finishes_map[finish] = []
        finishes_map[finish].append(molecule)

    starts = sorted(starts_map.keys())
    finishes = sorted(finishes_map.keys())

    intersections = {}
    current_molecules = set()

    i = 0
    j = 0
    while i < len(starts) and j < len(finishes):
        if starts[i] < finishes[j]:
            current_molecules.update(starts_map[starts[i]])
            intersections[starts[i]] = list(current_molecules)
            i += 1
        elif starts[i] > finishes[j]:
            current_molecules.difference_update(finishes_map[finishes[j]])
            intersections[finishes[j]] = list(current_molecules)
            j += 1
        else:
            current_molecules.update(starts_map[starts[i]])
            current_molecules.difference_update(finishes_map[finishes[j]])
            intersections[starts[i]] = list(current_molecules)
            i += 1
            j += 1

    while i < len(starts):
        current_molecules.update(starts_map[starts[i]])
        intersections[starts[i]] = list(current_molecules)
        i += 1

    while j < len(finishes):
        current_molecules.difference_update(finishes_map[finishes[j]])
        intersections[finishes[j]] = list(current_molecules)
        j += 1

    for intersection in intersections:
        intersections[intersection].sort()

    return intersections


def main(args):
    if len(args) != 3:
        print("Usage: python find_molecul_intersections.py <input_file_name> <output_file_name>")
        return

    input_file_name = args[1]
    output_file_name = args[2]

    # if input file does not exist fail with error
    if not os.path.exists(input_file_name):
        print(f'File {input_file_name} does not exist')
        return

    # if output file exists fail with error
    if os.path.exists(output_file_name):
        print(f'File {output_file_name} already exists')
        return

    lines = read_csv(input_file_name)
    data = parse_data(lines)
    intersection_results = find_intersections(data)

    with open(output_file_name, 'w') as f:
        for time, molecules in intersection_results.items():
            f.write(f'{time}, {len(molecules)}, "{" ".join(molecules)}"\n')

    # Plot the graph
    plot_intersections(intersection_results)
    print("Done")

if __name__ == '__main__':
    main(sys.argv)

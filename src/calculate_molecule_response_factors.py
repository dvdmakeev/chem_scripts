import os
import sys


# ./calculate_molecules_response_factors.py response_factors.csv molecules.csv output.csv
#
# molecules.csv file format
# 15:0-15:0-15:0
# 17:0-17:0-17:0
#
# response_factors.csv file format
# 15:0 0.1
# 17:0 5
#
# Expected result:
# 15:0-15:0-15:0 0.1
# 17:0-17:0-17:0 5


def read_response_factors_file(file_name):
    response_factors = {}
    with open(file_name, "r") as f:
        for line in f:
            fragment, response_factor = line.strip().split()
            if fragment in response_factors:
                print(f"Duplicate fragment {fragment} in response factors file")
                return

            response_factors[fragment] = float(response_factor)

    return response_factors


def read_molecules_file(file_name):
    molecules = []
    with open(file_name, "r") as f:
        for line in f:
            molecules.append(line.strip())

    return molecules


def write_output_file(file_name, molecules_response_factors):
    with open(file_name, "w") as f:
        for molecule, response_factor in molecules_response_factors.items():
            f.write(f"{molecule} {response_factor}\n")


def calculate_molecules_response_factors(molecules, response_factors):
    # Molecule's response factor is an average of response factors of its fragments
    molecules_response_factors = {}
    for molecule in molecules:
        fragments = molecule.split("-")
        response_factor = 0

        for fragment in fragments:
            if fragment not in response_factors:
                raise ValueError(f"Fragment {fragment} not found in response factors file")

            response_factor += response_factors[fragment]

        response_factor /= len(fragments)
        molecules_response_factors[molecule] = response_factor

    return molecules_response_factors


def main(args):
    if len(args) != 4:
        print("Usage: python calculate_molecules_response_factors.py <response_factors_file_name> <molecules_file_name>")
        return

    response_factors_file_name = args[1]
    molecules_file_name = args[2]
    output_file_name = args[3]

    if not os.path.exists(response_factors_file_name):
        print(f"File {response_factors_file_name} does not exist")
        return

    if not os.path.exists(molecules_file_name):
        print(f"File {molecules_file_name} does not exist")
        return

    if os.path.exists(output_file_name):
        print(f"File {output_file_name} already exists")
        return

    response_factors = read_response_factors_file(response_factors_file_name)
    molecules = read_molecules_file(molecules_file_name)

    try:
        molecules_response_factors = calculate_molecules_response_factors(molecules, response_factors)
    except ValueError as e:
        print(e)
        return

    write_output_file(output_file_name, molecules_response_factors)
    print(f"Output written to {output_file_name}")


if __name__ == "__main__":
    main(sys.argv)

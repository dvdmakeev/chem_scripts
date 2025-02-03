import pytest

from find_molecul_intersections import find_intersections


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

def test_find_molecule_intersections():
    data = [
        {'molecule': 'A', 'start': 0, 'finish': 5},
        {'molecule': 'B', 'start': 2, 'finish': 4},
        {'molecule': 'C', 'start': 3, 'finish': 6},
        {'molecule': 'D', 'start': 5, 'finish': 7},
    ]
    expected_result = {
        0: ['A'],
        2: ['A', 'B'],
        3: ['A', 'B', 'C'],
        4: ['A', 'C'],
        5: ['C', 'D'],
        6: ['D'],
        7: [],
    }

    result = find_intersections(data)

    # sort molecules in the result
    for key in result:
        result[key].sort()

    assert result == expected_result


def test_find_molecule_intersections_empty():
    data = []
    expected_result = {}
    result = find_intersections(data)
    assert result == expected_result

def test_find_molecule_intersections_single():
    data = [
        {'molecule': 'A', 'start': 0, 'finish': 5},
    ]
    expected_result = {
        0: ['A'],
        5: [],
    }
    result = find_intersections(data)

    for key in result:
        result[key].sort()
    assert result == expected_result

def test_find_molecule_intersections_no_overlap():
    data = [
        {'molecule': 'A', 'start': 0, 'finish': 2},
        {'molecule': 'B', 'start': 3, 'finish': 5},
    ]
    expected_result = {
        0: ['A'],
        2: [],
        3: ['B'],
        5: [],
    }
    result = find_intersections(data)
    # sort molecules in the result
    for key in result:
        result[key].sort()
    assert result == expected_result

def test_find_molecule_intersections_full_overlap():
    data = [
        {'molecule': 'A', 'start': 0, 'finish': 5},
        {'molecule': 'B', 'start': 0, 'finish': 5},
    ]
    expected_result = {
        0: ['A', 'B'],
        5: [],
    }
    result = find_intersections(data)

    for key in result:
        result[key].sort()

    assert result == expected_result

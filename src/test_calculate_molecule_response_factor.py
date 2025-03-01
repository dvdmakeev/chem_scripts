import pytest
from calculate_molecule_response_factors import calculate_molecules_response_factors


def test_calculate_molecule_response_factor():
    molecules = [
        '15:1-15:2-15:5',
        '17:0-17:1-17:2',
    ]
    response_factors = {
        '15:1': 0.2,
        '15:2': 0.3,
        '15:5': 0.5,
        '17:0': 0.1,
        '17:1': 5,
        '17:2': 10,
    }
    expected_result = {
        '15:1-15:2-15:5': 0.3333333333333333,
        '17:0-17:1-17:2': 5.033333333333333
    }

    result = calculate_molecules_response_factors(molecules, response_factors)

    assert result == expected_result


def test_calculate_molecule_response_factor_empty():
    molecules = []
    response_factors = {}
    expected_result = {}

    result = calculate_molecules_response_factors(molecules, response_factors)

    assert result == expected_result


def test_calculate_molecule_response_factor_single():
    molecules = [
        '15:0-15:0-15:0',
    ]
    response_factors = {
        '15:0': 0.1,
    }
    expected_result = {
        '15:0-15:0-15:0': 0.10000000000000002,
    }

    result = calculate_molecules_response_factors(molecules, response_factors)

    assert result == expected_result


def test_calculate_molecule_response_factor_missing_fragment_value_error():
    molecules = [
        '15:0-15:1-15:2',
    ]
    response_factors = {
        '15:0': 0.1,
    }

    with pytest.raises(ValueError):
        calculate_molecules_response_factors(molecules, response_factors)

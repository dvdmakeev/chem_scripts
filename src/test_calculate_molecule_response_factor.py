import pytest
from calculate_molecule_response_factors import calculate_molecules_response_factors, validate_molecules_response_factors


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
        '15:1-15:2-15:5': 0.3333,
        '17:0-17:1-17:2': 5.0333
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
        '15:0-15:0-15:0': 0.1000,
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


def test_validate_molecules_response_factors():
    molecules = [
        '15:0-15:1-15:2',
        '17:0-17:1-17:2',
    ]
    response_factors = {
        '15:0': 0.1,
        '15:1': 0.2,
        '15:2': 0.3,
        '17:0': 0.1,
        '17:1': 5,
        '17:2': 10,
    }

    result = validate_molecules_response_factors(molecules, response_factors)

    assert result == None


def test_validate_molecules_response_factors_missing_fragment():
    molecules = [
        '15:0-15:1-15:2',
        '17:0-17:1-17:2',
    ]
    response_factors = {
        '15:0': 0.1,
        '15:1': 0.2,
        '17:0': 0.1,
        '17:1': 5,
        '17:2': 10,
    }

    result = validate_molecules_response_factors(molecules, response_factors)

    assert result == {'15:2': ['15:0-15:1-15:2']}


import sys
import os
import random
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import get_player_guess, get_computer_guess, check_number, get_updated_bound

random.seed(42)

@pytest.mark.parametrize("player_input, expected_guess", [("42", 42), ("50", 50)])
@patch("builtins.input")
def test_get_player_guess(mock_input, player_input, expected_guess):
    mock_input.return_value = player_input
    guess = get_player_guess()
    mock_input.assert_called_once()
    assert guess == expected_guess


@pytest.mark.parametrize(
    "lower_bound, upper_bound, expected_guess",
    [(1, 100, 50), (50, 100, 75), (1, 50, 25), (16, 84, 50), (37, 92, 64)],
)
def test_get_computer_guess(lower_bound, upper_bound, expected_guess):
    assert get_computer_guess(lower_bound, upper_bound) == expected_guess


@pytest.mark.parametrize(
    "secret_number, guess, expected_result",
    [(50, 50, "correct"), (50, 25, "higher"), (50, 75, "lower")],
)
def test_check_number(secret_number, guess, expected_result):
    assert check_number(secret_number, guess) == expected_result


@pytest.mark.parametrize(
    "guess, result, expected_bound", [(50, "higher", 51), (50, "lower", 49)]
)
def test_get_updated_bound(guess, result, expected_bound):
    assert get_updated_bound(guess, result) == expected_bound

import random
import pytest

from unittest.mock import patch

from main import game, show_results

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


@pytest.mark.parametrize(
    "round_count, player_tries, computer_tries", [(2, [1, 2], [3])]
)
def test_raise_index_error(round_count, player_tries, computer_tries, capsys):
    show_results(round_count, player_tries, computer_tries)
    
    captured = capsys.readouterr()
    
    assert "Computer do not make move in this round" in captured.out


def test_game(capsys):
    with patch("main.get_secret_number") as mock_get_secret_number, patch(
        "main.get_player_guess"
    ) as mock_get_player_guess, patch("main.get_computer_guess") as mock_get_computer_guess, patch("main.show_results") as mock_show_results:
        mock_get_secret_number.return_value = 42
        mock_get_player_guess.side_effect = [50, 25, 42]
        mock_get_computer_guess.side_effect = [26, 30]
        
        game()
        
        captured = capsys.readouterr()
        
        assert mock_get_secret_number.call_count == 1
        assert mock_get_player_guess.call_count == 3
        assert mock_get_computer_guess.call_count == 2
        
        mock_show_results.assert_called_once_with(3, [50, 25, 42], [26, 30])
        
        assert "Congratulation! You won the game the secret numbre is 42" in captured.out
        

import unittest
from unittest.mock import patch
import random
from main import (
    get_player_guess,
    get_computer_guess,
    check_number,
    get_secret_number,
    game,
    get_updated_bound,
    show_results,
)

import io
from contextlib import redirect_stdout


class TestGuessGame(unittest.TestCase):

    def setUp(self):
        random.seed(42)

    @patch("builtins.input", return_value="42")
    def test_get_player_guess_is_int_value(self, mock_input):
        guess = get_player_guess()
        mock_input.assert_called_once()
        self.assertIsInstance(guess, int)
        self.assertEqual(guess, 42)

    @patch("builtins.input", return_value="abc")
    def test_get_player_guess_text_raise_error(self, mock_input):
        self.assertRaises(ValueError, get_player_guess)

    @patch("builtins.input", return_value="4.5")
    def test_get_player_guess_float_raise_error(self, mock_input):
        self.assertRaises(ValueError, get_player_guess)

    def test_get_computer_guess_return_mid_value(self):
        self.assertEqual(get_computer_guess(1, 100), 50)
        self.assertEqual(get_computer_guess(50, 100), 75)
        self.assertEqual(get_computer_guess(1, 50), 25)
        self.assertEqual(get_computer_guess(16, 84), 50)
        self.assertEqual(get_computer_guess(37, 92), 64)

    def test_check_number(self):
        self.assertEqual(check_number(50, 50), "correct")
        self.assertEqual(check_number(50, 25), "higher")
        self.assertEqual(check_number(50, 75), "lower")

    def test_get_updated_bound_adds_or_subtracts_one(self):
        self.assertEqual(get_updated_bound(50, "higher"), 51)
        self.assertEqual(get_updated_bound(50, "lower"), 49)

    @patch("main.get_secret_number", return_value=42)
    @patch("main.get_player_guess", side_effect=[1, 2, 42])
    @patch("main.get_computer_guess", return_value=22)
    @patch("main.show_results")
    def test_play_game_turn(
        self,
        mock_show_results,
        mock_get_computer_guess,
        mock_get_player_guess,
        mock_get_secret_number
    ):
        """
        Test play_game
        Tests that the player and computer guess functiones
        are called in turns, amount of times as expected until play ends
        """
        game()
        assert mock_get_secret_number.call_count == 1
        assert mock_get_computer_guess.call_count == 2
        assert mock_get_player_guess.call_count == 3
        mock_show_results.assert_called_once()
        
    def test_show_results(self):
        round_count = 3
        player_tries = [10, 20, 30]
        computer_tries = [15, 25]
        
        with io.StringIO() as buffer, redirect_stdout(buffer):
            show_results(round_count, player_tries, computer_tries)
            output = buffer.getvalue()

        expected_output = """--- Results ---
This is the results in the game:
In Total was 3 rounds

1th Round:
Player choose: 10
Computer choose: 15

2th Round:
Player choose: 20
Computer choose: 25

3th Round:
Player choose: 30
Computer do not make move in this round
"""
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()

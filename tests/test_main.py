import unittest
from unittest.mock import patch
import io
import random
from main import (
    get_player_guess,
    get_computer_guess,
    check_number,
    get_updated_bound,
)


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
        
    # def test_


if __name__ == "__main__":
    unittest.main()

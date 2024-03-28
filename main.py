"""
Aplicación para adiviar un numero
"""
import random

def player_guess(secret_number):
    """Permite al usuario ingresar un valor y luego verifica si es el numero correcto"""
    try:
        guess = int(input("--- Round: Player 1 ---\nPlayer 1, enter your guess: \n"))
        result = check_number(secret_number, guess)
        if result == "correct":
            return True
    except ValueError:
        print("Please enter a valid number!")


def computer_guess(secret_number, lower_bound, upper_bound):
    guess = random.randint(lower_bound, upper_bound)
    print(f"--- Round: Computer ---\nComputer guess: {guess}\n")
    result = check_number(secret_number, guess, "Computer")
    if result == "correct":
        return result
    else:
        info = {"guess": guess, "response": result}
        return info


def check_number(secret_number, guess, player="You"):
    if guess == secret_number:
        print(f"Congratulations! {player} guessed the secret number!\n")
        return "correct"
    elif guess < secret_number:
        print("Too low.\n")
        return "higher"
    else:
        print("Too high.\n")
        return "lower"


def main():
    secret_number = random.randint(1, 100)
    is_player_turn = True
    is_finished = False
    lower_bound = 1
    upper_bound = 100

    while not is_finished:
        if is_player_turn:
            is_finished = player_guess(secret_number)
        else:
            result = computer_guess(secret_number, lower_bound, upper_bound)
            if result == "correct":
                is_finished = True
            else:
                if result["response"] == "lower":
                    upper_bound = result["guess"] - 1
                else:
                    lower_bound = result["guess"] + 1
        is_player_turn = not is_player_turn


if __name__ == "__main__":
    main()

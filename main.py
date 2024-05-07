import random

def get_secret_number():
    return random.randint(1, 100)

def get_player_guess():
    """Permite al usuario ingresar un valor y retorna ese valor"""
    player_guess = int(input("Enter a guess: "))

    return player_guess


def get_computer_guess(lower_bound, upper_bound):
    """Retorna una decisión tomando el punto medio de un rango"""
    mid_guess = (lower_bound + upper_bound) // 2
    return mid_guess


def check_number(secret_number, guess):
    """Verificá si el intento coincide con el número secreto"""
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "higher"
    else:
        return "lower"


def get_updated_bound(guess, result):
    """Función para actualizar los randos de elección según los resultados"""
    if result == "higher":
        return guess + 1
    else:
        return guess - 1


def show_results(round_count, player_tries, computer_tries):
    """Función que muestra todas las elecciones hechas durante el juego"""
    print("--- Results ---\nThis is the results in the game:")
    print(f"In Total was {round_count} rounds\n")
    for _round in range(round_count):
        print(f"{_round + 1}th Round:")
        print(f"Player choose: {player_tries[_round]}")
        try:
            print(f"Computer choose: {computer_tries[_round]}\n")
        except IndexError:
            print("Computer do not make move in this round")

def show_round(round_count, player_guess, player):
    print(f"--- Round {round_count}: {player} ---\n{player} guess is: {player_guess}")


def show_round_result(result, secret_number):
    if result == "correct":
        print(
            f"Congratulation! You won the game the secret numbre is {secret_number}\n"
        )
    elif result == "higher":
        print("Sorry! too low\n")
    else:
        print("Sorry! too high\n")


def game():
    secret_number = get_secret_number()
    is_player_turn = True
    is_finished = False
    lower_bound = 1
    upper_bound = 100
    round_count = 1
    player_tries = []
    computer_tries = []

    # El loop se repetirá hasta que la variable is_finished sea verdadera
    while not is_finished:
        if is_player_turn:
            guess = None
            while guess is None:
                try:
                    guess = get_player_guess()
                except ValueError:
                    print("Ingresa un numero entero")
            show_round(round_count, guess, "player 1")
            player_tries.append(guess)
            result = check_number(secret_number, guess)
            show_round_result(result, secret_number)
            
        else:
            guess = get_computer_guess(lower_bound, upper_bound)
            show_round(round_count, guess, "Computer")
            computer_tries.append(guess)
            result = check_number(secret_number, guess)
            show_round_result(result, secret_number)
            round_count += 1

        if result == "correct":
            is_finished = True
            show_results(round_count, player_tries, computer_tries)
        elif result == "higher":
            lower_bound = get_updated_bound(guess, result)
        else:
            upper_bound = get_updated_bound(guess, result)

        is_player_turn = not is_player_turn


if __name__ == "__main__":
   game()

import random

def get_player_guess(round):
    """Permite al usuario ingresar un valor y retorna ese valor"""
    player_guess = None

    while player_guess == None:
        try:
            player_guess = int(
                input(f"--- Round {round}: Player 1 ---\nPlayer 1, enter your guess: ")
            )
        except:
            print("Enter a correct number\n")

    return player_guess


def get_computer_guess(lower_bound, upper_bound, round_count):
    """Retorna una decisión tomando el punto medio de un rango"""
    mid_guess = round((lower_bound + upper_bound) / 2)
    return mid_guess


def check_number(secret_number, guess):
    """Verificá si el intento coincide con el número secreto"""
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "higher"
    else:
        return "lower"


def updated_bound(player_guess, result):
    """Función para actualizar los randos de elección según los resultados"""
    if result == "higher":
        return player_guess + 1
    else:
        return player_guess - 1


def show_result(round_count, player_tries, computer_tries):
    """Función que muestra todas las elecciones hechas durante el juego"""
    print("--- Results ---\nThis is the results in the game:")
    print(f"In Total was {round_count} rounds\n")
    for _round in range(round_count):
        print(f"{_round + 1}th Round:")
        print(f"Player choose: {player_tries[_round]}")
        try:
            print(f"Computer choose: {computer_tries[_round]}\n")
        except:
            print("Computer did not make any choice in this round\n")


def main():
    secret_number = random.randint(1, 100)
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

            player_guess = get_player_guess(round_count)
            player_tries.append(player_guess)
            result = check_number(secret_number, player_guess)

            if result == "correct":
                print(
                    f"Congratulation! You won the game the secret numbre is {secret_number}\n"
                )
                is_finished = True
                show_result(round_count, player_tries, computer_tries)
            elif result == "higher":
                print("Sorry! too low\n")
                lower_bound = updated_bound(player_guess, result)
            else:
                print("Sorry! too high\n")
                upper_bound = updated_bound(player_guess, result)
        else:

            computer_guess = get_computer_guess(lower_bound, upper_bound, round_count)
            print(
                f"--- Round {round_count}: Computer ---\nComputer guess is: {computer_guess}"
            )
            computer_tries.append(computer_guess)
            result = check_number(secret_number, computer_guess)

            if result == "correct":
                print(
                    f"Sorry! Computer won the game, the secret numbre is {secret_number}\n"
                )
                is_finished = True
                show_result(round_count, player_tries, computer_tries)
            elif result == "higher":
                print("Computer guess was too low\n")
                lower_bound = updated_bound(computer_guess, result)
            else:
                print("Computer guess was too high\n")
                upper_bound = updated_bound(computer_guess, result)

            round_count += 1
        is_player_turn = not is_player_turn


if __name__ == "__main__":
    main()

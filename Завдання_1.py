import random

def generate_secret_code():
    digits = list("0123456789")
    random.shuffle(digits)
    return digits[:4]

def get_hint(secret_code, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_code[i]:
            bulls += 1
        elif guess[i] in secret_code:
            cows += 1
    return bulls, cows

def is_valid_guess(guess):
    return guess.isdigit() and len(guess) == 4

def play_game():
    print("Вітаю у грі 'Таємний код'!")
    print("Спробуйте вгадати 4-цифровий код з унікальними цифрами.")
    secret_code = generate_secret_code()

    attempts = 0
    while True:
        guess = input("Введіть ваше припущення (4 цифри): ")
        if not is_valid_guess(guess):
            print("Невірний формат. Введіть рівно 4 цифри.")
            continue

        guess_list = list(guess)
        attempts += 1
        bulls, cows = get_hint(secret_code, guess_list)

        print(f"Бики: {bulls}, Корови: {cows}")

        if bulls == 4:
            print(f"Ви вгадали код за {attempts} спроб! Вітаю!")
            break

if __name__ == "__main__":
    play_game()

import tkinter as tk
from tkinter import messagebox
import random

def generate_secret_code():
    digits = list("0123456789")
    random.shuffle(digits)
    return digits[:4]

def get_hint(secret_code, guess):
    bulls = sum(guess[i] == secret_code[i] for i in range(4))
    cows = sum(1 for i in range(4) if guess[i] in secret_code and guess[i] != secret_code[i])
    return bulls, cows

class SecretCodeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Гра 'Таємний код'")
        self.secret_code = generate_secret_code()
        self.attempts = 0

        self.label = tk.Label(root, text="Введіть 4-цифровий код:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Спробувати", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_text = tk.Text(root, height=10, width=40, state='disabled', bg="#f0f0f0")
        self.result_text.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit() or len(guess) != 4:
            messagebox.showwarning("Помилка", "Введіть рівно 4 цифри.")
            return

        self.attempts += 1
        guess_list = list(guess)
        bulls, cows = get_hint(self.secret_code, guess_list)

        self.result_text.configure(state='normal')
        self.result_text.insert(tk.END, f"{guess} -> Бики: {bulls}, Корови: {cows}\n")
        self.result_text.configure(state='disabled')

        self.entry.delete(0, tk.END)

        if bulls == 4:
            messagebox.showinfo("Вітаємо!", f"Ви вгадали код за {self.attempts} спроб!")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = SecretCodeGame(root)
    root.mainloop()

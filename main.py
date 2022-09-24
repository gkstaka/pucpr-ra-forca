import random
import os
category_1 = ("cachorro", "gato")
category_2 = ("vinho", "cerveja")

categories = {
    "animais": category_1,
    "bebidas": category_2
}


def clear_console():
    os.system("cls")

def get_word():
    while True:
        print("""Categorias:
    [1] - Animais
    [2] - Bebidas
    """)
        choice = input("Escolha a categoria: ")
        try:
            if choice.isalpha():
                return random.choice(categories[choice.lower()])
            elif choice.isdigit() and int(choice) in range(1, len(categories) + 1):
                categories_list = list(categories.items())  # index = list(categories.items())
                return random.choice(categories_list[(int(choice) - 1)][1])  # print(random.choice(index[0][1]))
        except:
            print("Entrada invalida. Tente novamente.")


def remaining_letters(word_string):
    count = 0
    for i in word_string:
        if i == "_":
            count += 1
    return count


word = get_word()
word_output = ["_"] * len(word)
guess = []
formated_word = ""
wrong_guess = 0
print(f"Palavra: {''.join(word_output)}\t- \t{remaining_letters(word_output)} letras restantes", end="\n\n")
while True:
    clear_console()
    print(f"Letras ja escolhidas: {sorted(guess)}")
    print(f"Erros: {wrong_guess}")
    letter = input("A letra que deseja chutar: ")
    letter = letter.strip(" ")
    letter = letter.lower()
    if letter.isalpha() and len(letter) == 1 and letter not in guess:
        guess.append(letter)
        flag = False
        for i, c in enumerate(word):
            if c == (letter):
                # print("Letra encontrada")
                # print(i, c)
                word_output[i] = c
                flag = True
        if flag is False:
            print("Letra nao presente na palavra")
            wrong_guess += 1
            # print(f"Erros: {wrong_guess}")
            # print(f"Letra valida.")
    elif letter in guess:
        print("Letra6 repetida")
    else:
        print("Entrada invalida")
    formated_word = "".join(word_output)
    # print(word_output)
    print()
    print(f"Palavra: {formated_word}\t- \t{remaining_letters(formated_word)} letras restantes")
    if "_" not in word_output:
        break

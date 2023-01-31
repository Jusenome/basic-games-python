import getpass
from hangman_diagrams import lifes_dictionary_visual

def hangman():
  play : str = "si"
  while play == "si":
    print("================================")
    print(" Bienvenido al juego el ahorcado ")
    print("================================ \n")
    
    
    correct : bool = False
    lifes : int = 7
    
    word_guess = getpass.getpass("Ingrese la palabra a adivinar: ").upper()
    string_empty = "_" * len(word_guess)
    print(f"La palabra a encontrar tiene {len(word_guess)} letras \n")
    
    print(f"Tienes {lifes} intentos")

    while correct == False and lifes > 0:
      print(f"Adivina la palabra: {string_empty} \n")
      letter_input = input("Ingrese una letra: ").upper()

      if letter_input in word_guess:
        positions = [i for i, letter_word in enumerate(word_guess) if letter_word == letter_input]
        list_letters = list(string_empty)
        for p in positions:
          list_letters[p] = letter_input
        string_empty = "".join(list_letters)
      else:
        print("La letra no se encuentra en la palabra")
        lifes -= 1
        print(lifes_dictionary_visual[lifes])

        if lifes == 0:
          print("Lo siento. Has perdido\n")
          print(f"La palabra era {word_guess}")
          print("*" * 40)

      if string_empty == word_guess:
        print(string_empty)
        print("Felicidades! Has ganado \n")
        correct = True

    play = input("¿Quiere seguir jugando? Digite si (continuar) o no (para salir) \n").lower()


if __name__ == "__main__":
  hangman()

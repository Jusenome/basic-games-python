import random

def guess_the_number(number):
  print("===============")
  print(" Bienvenido(a) al Juego ")
  print("=============== \n")

  print("Debes adivinar el número generado por la computadora \n")

  num_random : int = random.randint(1, number)
  prediction : int = 0
  cont : int = 0

  while prediction != num_random:
    prediction = int(input(f"Adivina un número entre 1 y {number}: "))

    cont += 1

    if prediction > num_random:
      print("Intenta de nuevo. Este núemero es mayor al generado por la computadora")
    elif prediction < num_random:
      print("Intenta de nuevo. Este núemero es menor al generado por la computadora")
    else:
      print(f"¡Felicidades! Has ganado el juego. {prediction} es el número correcto")

  return cont

if __name__ == "__main__":
  result = guess_the_number(1000000)
  print(f"Ha adivinado el número luego de {result} intentos")
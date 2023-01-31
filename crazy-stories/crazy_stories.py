# Concatenar cadena de caracteres

print("Mad Libs \n")

adj : str = "____________"
verb1 : str = "____________"
verb2 : str = "____________"
plural_noun : str = "____________"

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verb1} problemas. ¡Aprende a {verb2} con FreeCodeCamp y alcanza tus {plural_noun}!"

print("Completa la siguiente frase: \n" + madlib)

adj = input("Adjetivo: ")
verb1 = input("Verbo 1: ")
verb2 = input("Verbo 2: ")
plural_noun = input("Sustantivo plural: ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verb1} problemas. ¡Aprende a {verb2} con FreeCodeCamp y alcanza tus {plural_noun}!"

print("Tu frase ha quedado asi: \n" + madlib)


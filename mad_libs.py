adjetivo = input("Escreva um adjetivo: ")
cor = input("Escreva uma cor: ")
animal = input("Escreva o nome de um animal: ")
verbo = input("Escreva um verbo: ")
cidade = input("Escreva o nome de uma cidade: ")
subst = input("Escreva um substantivo: ")
comida = input("Escreva uma comida: ")
numero = input("Escreva um número: ")


madlibs = f"""Era uma vez um(a) {adjetivo} {animal},
que tinha uma cor {cor} que adorava {verbo}. 
Um certo dia, ele/ela viajou para uma {cidade},
e encontrou um(a) {subst} mágico(a).
Juntos, comeram {comida} e viveram {numero} anos felizes.
"""

print(madlibs)

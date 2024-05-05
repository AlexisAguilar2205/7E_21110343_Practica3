import random

class ClueSimulator:
    def __init__(self):
        self.personajes = {
            "Profesor Plum": {
                "profesion": "historiador",
                "pregunta": "Cual es su opinion sobre crimenes historicos famosos?",
                "respuesta": "El Profesor Plum está interesado en casos no resueltos del pasado, sugiere que ha investigado sobre el tema."
            },
            "Miss Scarlet": {
                "profesion": "actriz",
                "pregunta": "¿Qué estaba haciendo en la noche del crimen?",
                "respuesta": "Miss Scarlet dice que estaba ensayando para una obra de teatro, pero su coartada parece débil."
            },
            "Coronel Mustard": {
                "profesion": "militar retirado",
                "pregunta": "¿Tiene experiencia con armas de fuego?",
                "respuesta": "El Coronel Mustard admite haber sido un experto en el uso de armas, pero niega cualquier participación en el crimen."
            },
            "Mrs. White": {
                "profesion": "empleada doméstica",
                "pregunta": "¿Qué sabe sobre los rincones secretos de la mansión?",
                "respuesta": "Mrs. White revela que conoce todos los secretos de la mansión, pero asegura que no ha visto nada sospechoso."
            },
            "Mr. Green": {
                "profesion": "empresario",
                "pregunta": "¿Cómo podría haberse beneficiado de este crimen?",
                "respuesta": "Mr. Green sugiere que el crimen podría ser beneficioso para sus negocios, pero niega cualquier participación."
            }
        }
        self.locaciones = ["Mansión", "Hotel", "Restaurante", "Teatro", "Biblioteca"]
        self.armas = ["Candelabro", "Cuchillo", "Revólver", "Cuerda", "Llave inglesa"]
        self.culpable = None
        self.arma_culpable = None
        self.locacion_culpable = None

    def generar_misterio(self):
        self.culpable = random.choice(list(self.personajes.keys()))
        self.arma_culpable = random.choice(self.armas)
        self.locacion_culpable = random.choice(self.locaciones)

    def jugar(self):
        print("Bienvenido al juego Clue. Se ha cometido un crimen misterioso.")
        print("Debe determinar quién es el culpable, con qué arma y en qué locación.")
        print("\nLas locaciones son:", self.locaciones)
        print("Las armas son:", self.armas)

        intentos = 0
        while True:
            intentos += 1
            print("\nIntento #", intentos)
            print("Pistas sobre los sospechosos:")
            for personaje, info in self.personajes.items():
                print(f"- {personaje}, {info['profesion']}: {info['pregunta']}")
            print()

            personaje = input("¿Quién crees que es el culpable? ")
            arma = input("¿Qué arma crees que se usó? ")
            locacion = input("¿En qué locación crees que ocurrió el crimen? ")

            if personaje == self.culpable and arma == self.arma_culpable and locacion == self.locacion_culpable:
                print("\n¡Felicidades! Has resuelto el misterio.")
                break
            else:
                print("\nIncorrecto. El misterio continúa...")
                if personaje in self.personajes:
                    print(self.personajes[personaje]["respuesta"])
                else:
                    print("No tienes suficiente información sobre este sospechoso.")

if __name__ == "__main__":
    juego = ClueSimulator()
    juego.generar_misterio()
    juego.jugar()


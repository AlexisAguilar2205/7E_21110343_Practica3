import random

class ClueSimulator:
    def __init__(self):
        self.personajes = {
            "Profesor Plum": {
                "profesion": "historiador",
                "pregunta": "Cual es su opinion sobre crimenes historicos famosos?",
                "respuesta": "El Profesor Plum est� interesado en casos no resueltos del pasado, sugiere que ha investigado sobre el tema."
            },
            "Miss Scarlet": {
                "profesion": "actriz",
                "pregunta": "�Qu� estaba haciendo en la noche del crimen?",
                "respuesta": "Miss Scarlet dice que estaba ensayando para una obra de teatro, pero su coartada parece d�bil."
            },
            "Coronel Mustard": {
                "profesion": "militar retirado",
                "pregunta": "�Tiene experiencia con armas de fuego?",
                "respuesta": "El Coronel Mustard admite haber sido un experto en el uso de armas, pero niega cualquier participaci�n en el crimen."
            },
            "Mrs. White": {
                "profesion": "empleada dom�stica",
                "pregunta": "�Qu� sabe sobre los rincones secretos de la mansi�n?",
                "respuesta": "Mrs. White revela que conoce todos los secretos de la mansi�n, pero asegura que no ha visto nada sospechoso."
            },
            "Mr. Green": {
                "profesion": "empresario",
                "pregunta": "�C�mo podr�a haberse beneficiado de este crimen?",
                "respuesta": "Mr. Green sugiere que el crimen podr�a ser beneficioso para sus negocios, pero niega cualquier participaci�n."
            }
        }
        self.locaciones = ["Mansi�n", "Hotel", "Restaurante", "Teatro", "Biblioteca"]
        self.armas = ["Candelabro", "Cuchillo", "Rev�lver", "Cuerda", "Llave inglesa"]
        self.culpable = None
        self.arma_culpable = None
        self.locacion_culpable = None

    def generar_misterio(self):
        self.culpable = random.choice(list(self.personajes.keys()))
        self.arma_culpable = random.choice(self.armas)
        self.locacion_culpable = random.choice(self.locaciones)

    def jugar(self):
        print("Bienvenido al juego Clue. Se ha cometido un crimen misterioso.")
        print("Debe determinar qui�n es el culpable, con qu� arma y en qu� locaci�n.")
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

            personaje = input("�Qui�n crees que es el culpable? ")
            arma = input("�Qu� arma crees que se us�? ")
            locacion = input("�En qu� locaci�n crees que ocurri� el crimen? ")

            if personaje == self.culpable and arma == self.arma_culpable and locacion == self.locacion_culpable:
                print("\n�Felicidades! Has resuelto el misterio.")
                break
            else:
                print("\nIncorrecto. El misterio contin�a...")
                if personaje in self.personajes:
                    print(self.personajes[personaje]["respuesta"])
                else:
                    print("No tienes suficiente informaci�n sobre este sospechoso.")

if __name__ == "__main__":
    juego = ClueSimulator()
    juego.generar_misterio()
    juego.jugar()


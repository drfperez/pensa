"""
Pensa v0.1
Llenguatge de programació educatiu en català.
"""

class Pensa:

    def __init__(self, explicar=False):
        self.variables = {}
        self.explicar = explicar

    def explica(self, text):
        if self.explicar:
            print(f"[EXPLICA] {text}")

    def valor(self, text):

        text = text.strip()

        if text.startswith('"') and text.endswith('"'):
            return text[1:-1]

        try:
            return int(text)
        except ValueError:
            pass

        if text in self.variables:
            return self.variables[text]

        return text

    def avalua_condicio(self, condicio):

        operadors = [">=", "<=", "==", "!=", ">", "<"]

        for op in operadors:

            if op in condicio:

                esquerra, dreta = condicio.split(op)

                esquerra = self.valor(esquerra.strip())
                dreta = self.valor(dreta.strip())

                if op == ">":
                    return esquerra > dreta
                if op == "<":
                    return esquerra < dreta
                if op == ">=":
                    return esquerra >= dreta
                if op == "<=":
                    return esquerra <= dreta
                if op == "==":
                    return esquerra == dreta
                if op == "!=":
                    return esquerra != dreta

        raise Exception(f"Condició no vàlida: {condicio}")

    def executa_bloc(self, linies):

        i = 0

        while i < len(linies):

            linia = linies[i].strip()

            if not linia:
                i += 1
                continue

            # MOSTRA
            if linia.startswith("mostra "):

                contingut = linia[7:]
                valor = self.valor(contingut)

                self.explica(f"Mostro {valor}")

                print(valor)

            # GUARDA
            elif linia.startswith("guarda "):

                parts = linia[7:].split(" dins ")

                if len(parts) != 2:
                    raise Exception("Sintaxi incorrecta a guarda")

                valor = self.valor(parts[0])
                variable = parts[1].strip()

                self.variables[variable] = valor

                self.explica(
                    f"Guardo {valor} dins la variable {variable}"
                )

            # SI
            elif linia.startswith("si "):

                condicio = linia[3:]

                bloc_si = []
                bloc_no = []

                actual = bloc_si

                profunditat = 1

                i += 1

                while i < len(linies):

                    l = linies[i].strip()

                    if l.startswith("si "):
                        profunditat += 1

                    if l == "acaba":
                        profunditat -= 1

                        if profunditat == 0:
                            break

                    if profunditat == 1 and l == "si no":
                        actual = bloc_no
                        i += 1
                        continue

                    actual.append(linies[i])

                    i += 1

                resultat = self.avalua_condicio(condicio)

                self.explica(
                    f"La condició '{condicio}' és {resultat}"
                )

                if resultat:
                    self.executa_bloc(bloc_si)
                else:
                    self.executa_bloc(bloc_no)

            # REPETEIX
            elif linia.startswith("repeteix "):

                text = linia.replace("repeteix ", "")
                vegades = int(text.replace(" vegades", ""))

                bloc = []

                profunditat = 1

                i += 1

                while i < len(linies):

                    l = linies[i].strip()

                    if l.startswith("repeteix "):
                        profunditat += 1

                    if l == "acaba":
                        profunditat -= 1

                        if profunditat == 0:
                            break

                    bloc.append(linies[i])

                    i += 1

                self.explica(
                    f"Repeteixo {vegades} vegades"
                )

                for _ in range(vegades):
                    self.executa_bloc(bloc)

            else:
                raise Exception(
                    f"Instrucció desconeguda: {linia}"
                )

            i += 1

    def executa(self, codi):

        linies = codi.splitlines()
        self.executa_bloc(linies)


def executar_fitxer(nom_fitxer, explicar=False):

    with open(nom_fitxer, encoding="utf-8") as f:
        codi = f.read()

    pensa = Pensa(explicar)
    pensa.executa(codi)


if __name__ == "__main__":

    import sys

    if len(sys.argv) < 2:

        print("Ús:")
        print("python pensa.py programa.pensa")
        print("python pensa.py programa.pensa --explica")

        sys.exit(1)

    fitxer = sys.argv[1]

    explicar = "--explica" in sys.argv

    executar_fitxer(fitxer, explicar)

# 🧠 Pensa v0.4

> El llenguatge de programació educatiu en català per aprendre a pensar abans de programar.



# 📖 Què és Pensa?

**Pensa** és un llenguatge de programació educatiu dissenyat per ajudar estudiants a aprendre:

- Pensament computacional
- Algorismes
- Variables
- Condicions
- Bucles
- Funcions
- Estructures de dades

sense haver d'aprendre primer una sintaxi complicada.

L'objectiu és que el codi sigui tan llegible com sigui possible.

Per exemple:

```text
guarda 18 dins edat

si edat >= 18

    mostra "Ets major d'edat"

si no

    mostra "Ets menor d'edat"

acaba
```

Encara que mai hagis programat, probablement entens què fa.

---

# 🎯 Filosofia

La filosofia de Pensa és simple:

> Primer aprèn a pensar.
>
> Després aprendràs qualsevol altre llenguatge.

Els conceptes que s'aprenen amb Pensa es poden transferir fàcilment a:

- Python
- JavaScript
- Java
- C#
- C++
- Rust
- Go

i pràcticament qualsevol llenguatge modern.

---

# 🚀 Inici ràpid

## Requisits

- Python 3.10 o superior

Comprova la teva versió:

```bash
python --version
```

---

## Executar un programa

```bash
python pensa.py examples/demo.pensa
```

---

# 📝 Hola Món

Crea un fitxer:

```text
mostra "Hola món"
```

Executa'l:

```bash
python pensa.py hola.pensa
```

Resultat:

```text
Hola món
```

---

# 📦 Variables

Les variables permeten emmagatzemar dades.

## Crear una variable

```text
guarda 25 dins edat
```

Això crea una variable anomenada:

```text
edat
```

amb valor:

```text
25
```

---

## Mostrar una variable

```text
guarda 25 dins edat

mostra edat
```

Sortida:

```text
25
```

---

# 🔢 Operacions

## Sumar

```text
guarda 10 dins punts

suma 5 a punts

mostra punts
```

Resultat:

```text
15
```

---

## Restar

```text
guarda 10 dins vides

resta 2 a vides

mostra vides
```

Resultat:

```text
8
```

---

# 🤔 Condicions

Les condicions permeten prendre decisions.

## Exemple

```text
guarda 16 dins edat

si edat >= 18

    mostra "Adult"

si no

    mostra "Menor"

acaba
```

Resultat:

```text
Menor
```

---

## Operadors disponibles

```text
>
<
>=
<=
==
!=
```

---

## Operadors lògics

### I

```text
si nota >= 5 i nota < 10
```

### O

```text
si resposta == 1 o resposta == 2
```

---

# 🔁 Repeticions

## Repeteix

```text
repeteix 3 vegades

    mostra "Hola"

acaba
```

Resultat:

```text
Hola
Hola
Hola
```

---

# 🔄 Mentre

Permet repetir mentre una condició sigui certa.

```text
guarda 0 dins comptador

mentre comptador < 5

    mostra comptador

    suma 1 a comptador

acaba
```

Resultat:

```text
0
1
2
3
4
```

---

# 📚 Llistes

Una llista és un conjunt de valors.

## Crear una llista

```text
guarda [10,20,30] dins notes
```

---

## Mostrar una llista

```text
mostra notes
```

Resultat:

```text
[10,20,30]
```

---

# 🔍 Recorregut de llistes

## Per cada

```text
guarda [10,20,30] dins notes

per cada nota dins notes

    mostra nota

acaba
```

Resultat:

```text
10
20
30
```

---

# ⚙️ Funcions

Les funcions permeten reutilitzar codi.

## Definir una funció

```text
funcio saluda

    mostra "Hola"

acaba
```

---

## Executar una funció

```text
crida saluda
```

---

## Exemple complet

```text
funcio saluda

    mostra "Hola"

acaba

crida saluda
```

Resultat:

```text
Hola
```

---

# 💬 Comentaris

Els comentaris serveixen per explicar el programa.

Qualsevol línia que comenci amb:

```text
#
```

serà ignorada.

Exemple:

```text
# Aquest és un comentari

mostra "Hola"
```

---

# 📂 Exemple complet

```text
# Exemple de Pensa

mostra "Benvingut"

funcio saluda

    mostra "Hola alumne"

acaba

crida saluda

guarda [1,2,3] dins numeros

per cada numero dins numeros

    mostra numero

acaba

guarda 0 dins comptador

mentre comptador < 3

    mostra comptador

    suma 1 a comptador

acaba
```

Sortida:

```text
Benvingut
Hola alumne
1
2
3
0
1
2
```

---

# 🏗️ Arquitectura del projecte

```text
pensa/
│
├── pensa.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── interpreter.py
├── errors.py
│
├── examples/
│   └── demo.pensa
│
└── README.md
```

---

# 📌 Estat del projecte

Pensa v0.4 és una versió experimental.

Implementat:

- ✅ Variables
- ✅ Condicions
- ✅ Repeticions
- ✅ Funcions bàsiques
- ✅ Llistes
- ✅ Recorreguts
- ✅ Arquitectura modular

Previst per a futures versions:

- 🔜 Funcions amb paràmetres
- 🔜 Retorns (`retorna`)
- 🔜 Diccionaris
- 🔜 Classes i objectes
- 🔜 Imports
- 🔜 Traducció a Python
- 🔜 Diagrames de flux
- 🔜 Editor web
- 🔜 Extensió VS Code
- 🔜 Mode professor

---

# 🤝 Contribuir

Les contribucions són benvingudes.

Idees especialment interessants:

- Noves instruccions educatives
- Millor gestió d'errors
- Exercicis per a estudiants
- Traducció a altres idiomes
- Diagrames automàtics
- Integració amb entorns educatius

---

# 📜 Llicència

MIT License

Pots utilitzar, modificar i distribuir aquest projecte lliurement.

---

# ❤️ Pensa

> La programació no consisteix a escriure codi.
>
> Consisteix a aprendre a pensar de manera ordenada.
>
> **Pensa t'ajuda a fer aquest primer pas.**

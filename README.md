# 🧠 Pensa v0.5

> Aprèn a pensar. Després programa.

Pensa és un llenguatge de programació educatiu en català dissenyat per facilitar l'aprenentatge dels conceptes fonamentals de la programació d'una manera clara, intuïtiva i progressiva.

L'objectiu principal és ajudar l'alumne a desenvolupar pensament computacional abans de preocupar-se per sintaxis complexes.

---

# 🎯 Filosofia

La majoria de llenguatges obliguen a aprendre una sintaxi complicada abans d'entendre la programació. Pensa fa exactament el contrari.

En lloc d'escriure:

```python
resultat = suma(10, 5)
print(resultat)
```

escrius:

```text
guarda crida suma 10 5 dins resultat
mostra resultat
```

Això permet concentrar-se en els conceptes importants:

- Variables
- Funcions
- Paràmetres
- Retorns
- Algorismes
- Resolució de problemes

---

# 🚀 Instal·lació

## Requisits

- Python 3.10 o superior

Comprova la versió instal·lada:

```bash
python --version
```

---

# ▶ Executar un programa

```bash
python pensa.py programa.pensa
```

Exemple:

```bash
python pensa.py examples/demo.pensa
```

---

# 👋 Primer programa

## hola.pensa

```text
mostra "Hola món"
```

Resultat:

```text
Hola món
```

---

# 📦 Variables

Les variables serveixen per guardar informació.

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

Resultat:

```text
25
```

---

# 🔢 Nombres

Pensa suporta nombres enters.

Exemples:

```text
0
10
-5
100
```

---

# 📝 Text

Els textos s'escriuen entre cometes.

```text
"Hola"
"Barcelona"
"Programació"
```

Exemple:

```text
guarda "Francesc" dins nom
mostra nom
```

Resultat:

```text
Francesc
```

---

# ⚙️ Funcions

Les funcions permeten reutilitzar codi. Una funció és un bloc d'instruccions que es pot executar tantes vegades com sigui necessari.

---

# Crear una funció

```text
funcio saluda
    retorna "Hola"
acaba
```

---

# Executar una funció

```text
guarda crida saluda dins resultat
mostra resultat
```

Resultat:

```text
Hola
```

---

# 📥 Paràmetres

Els paràmetres permeten enviar informació a una funció.

## Exemple

```text
funcio identitat valor
    retorna valor
acaba
```

Execució:

```text
guarda crida identitat 10 dins resultat
mostra resultat
```

Resultat:

```text
10
```

---

# 📥📥 Dos paràmetres

```text
funcio suma a b
    retorna a + b
acaba
```

Execució:

```text
guarda crida suma 10 5 dins resultat
mostra resultat
```

Resultat:

```text
15
```

---

# 📥📥📥 Tres paràmetres

```text
funcio suma3 a b c
    retorna a + b + c
acaba
```

Execució:

```text
guarda crida suma3 1 2 3 dins resultat
mostra resultat
```

Resultat:

```text
6
```

---

# 🎁 Retornar valors

Les funcions poden retornar un valor mitjançant la instrucció:

```text
retorna
```

Exemple:

```text
funcio resposta
    retorna 42
acaba
```

Utilització:

```text
guarda crida resposta dins resultat
mostra resultat
```

Resultat:

```text
42
```

---

# ➕ Operacions matemàtiques

## Suma

```text
retorna a + b
```

---

## Resta

```text
retorna a - b
```

---

## Multiplicació

```text
retorna a * b
```

---

## Divisió

```text
retorna a / b
```

---

# Exemple: doble

```text
funcio doble x
    retorna x * 2
acaba
```

Execució:

```text
guarda crida doble 7 dins resultat
mostra resultat
```

Resultat:

```text
14
```

---

# Exemple complet

```text
funcio suma a b
    retorna a + b
acaba

funcio doble x
    retorna x * 2
acaba

guarda crida suma 10 5 dins resultat
mostra resultat

guarda crida doble resultat dins final
mostra final
```

Resultat:

```text
15
30
```

---

# 🔒 Variables locals

Els paràmetres d'una funció no modifiquen les variables globals.

Exemple:

```text
guarda 100 dins x

funcio prova x
    retorna x + 1
acaba

guarda crida prova 5 dins resultat
mostra resultat
mostra x
```

Resultat:

```text
6
100
```

La variable global continua valent:

```text
100
```

---

# ✅ Casos validats

La versió actual ha estat validada amb les proves següents:

### Funció simple

```text
funcio f
    retorna 1
acaba
```
✅ PASS

---

### Funció amb un paràmetre

```text
funcio identitat x
    retorna x
acaba
```
✅ PASS

---

### Funció amb dos paràmetres

```text
funcio suma a b
    retorna a + b
acaba
```
✅ PASS

---

### Funció amb tres paràmetres

```text
funcio suma3 a b c
    retorna a + b + c
acaba
```
✅ PASS

---

### Retorn de text

```text
funcio nom
    retorna "Francesc"
acaba
```
✅ PASS

---

### Variables locals

```text
guarda 100 dins x
funcio prova x
    retorna x + 1
acaba
```
✅ PASS

---

# ❌ Errors comuns

## Funció inexistent

Programa:

```text
crida noExisteix
```

Error:

```text
Funció inexistent: noExisteix
```

---

## Nombre incorrecte de paràmetres

Programa:

```text
funcio suma a b
    retorna a + b
acaba

guarda crida suma 10 dins resultat
```

Error:

```text
La funció suma necessita 2 paràmetres.
```

---

# 📂 Exemple de projecte

```text
projecte/
│
├── pensa.py
│
├── examples/
│   ├── hola.pensa
│   ├── suma.pensa
│   └── funcions.pensa
│
└── README.md
```

---

# ✅ Funcionalitats implementades

## Variables
```text
guarda
```

## Sortida
```text
mostra
```

## Funcions
```text
funcio
crida
retorna
```

## Assignació de resultats
```text
guarda crida suma 10 5 dins resultat
```

## Paràmetres
```text
funcio suma a b
```

## Expressions matemàtiques
```text
+
-
*
/
```

## Errors bàsics
```text
Funció inexistent
Nombre incorrecte de paràmetres
```

---

# 🚧 Limitacions actuals

Encara no estan implementats:

```text
si
si no
mentre
repeteix
llistes
per cada
imports
mòduls
AST complet
mode professor
IDE web
traductor a Python
```

---

# 🛣️ Full de ruta

## v0.6 Objectius:

```text
si
si no
mentre
repeteix
```

---

## v0.7 Objectius:

```text
llistes
per cada
text avançat
```

---

## v0.8 Objectius:

```text
imports
fitxers
mòduls
```

---

## v1.0 Objectius:

```text
AST complet
parser formal
depurador visual
IDE web
mode professor
traductor a Python
extensió VS Code
```

---

# ❤️ Pensa

> La programació no consisteix a memoritzar sintaxi.
>
> Consisteix a aprendre a resoldre problemes.
>
> Pensa t'ajuda a fer aquest primer pas.

# Tier (Animal) - Basisklasse

      |\_/|
     / @ @ \
    ( > 皿 < )
     `>>x<<´
    /  O  \

class Tier:
    def __init__(self, name, alter, geschlecht, gewicht):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht
        self.gewicht = gewicht
        self.gesund = True

    def vorstellen(self):
        return f"Hallo, ich bin {self.name}, ein {self.geschlecht}es Tier von {self.alter} Jahren und wiege {self.gewicht} kg."

    def fressen(self, nahrung):
        return f"{self.name} frisst {nahrung}."

    def trinken(self):
        return f"{self.name} trinkt Wasser."

    def bewegen(self):
        return f"{self.name} bewegt sich."

    def altern(self):
        self.alter += 1
        return f"{self.name} ist jetzt {self.alter} Jahre alt."

---

# Säugetier (Mammal) - Zwischenklasse

          .--.
         |o_o |
         |:_/ |
        //   \ \
       (|     | )
      /'\_   _/`\
      \___)=(___/

class Säugetier(Tier):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe):
        super().__init__(name, alter, geschlecht, gewicht)
        self.fellfarbe = fellfarbe
        self.hat_fell = True

    def säugen(self):
        return f"{self.name} säugt seine Jungen."

---

# Canidae (Hundeartige) - Unterfamilie von Säugetier

     /\_/\
    / o o \
   (   ^   )
    \_ U _/
      | |
      |_|

class Canidae(Säugetier):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, rudel_tier):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe)
        self.rudel_tier = rudel_tier # True, wenn es ein Rudeltier ist

    def kommunizieren(self):
        return f"{self.name} kommuniziert mit Lauten."

    def spuren_lesen(self):
        return f"{self.name} liest Spuren."

---

# Felidae (Katzenartige) - Unterfamilie von Säugetier

  /\_/\
 ( o.o )
  > ^ <

class Felidae(Säugetier):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, nachtaktiv):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe)
        self.nachtaktiv = nachtaktiv

    def schleichen(self):
        return f"{self.name} schleicht leise."

    def lauern(self, beute):
        return f"{self.name} lauert auf {beute}."

---

# Hund (Dog) - Unterklasse von Canidae

   __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/  \_)

class Hund(Canidae):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, rasse):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe, False) # Hunde sind oft keine reinen Rudeltiere in diesem Kontext
        self.rasse = rasse

    def bellen(self):
        return f"{self.name} bellt laut: Wuff! Wuff!"

    def apportieren(self, objekt):
        return f"{self.name} apportiert den {objekt}."

---

# Wolf (Wolf) - Unterklasse von Canidae

     /\_/\
    / o o \
   (   ^   )
    \_ U _/
      | |
      |_|

class Wolf(Canidae):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, rudelname):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe, True) # Wölfe sind Rudeltiere
        self.rudelname = rudelname

    def heulen(self):
        return f"{self.name} heult den Mond an."

    def jagen(self, beute):
        return f"{self.name} jagt {beute} im Rudel {self.rudelname}."

---

# Katze (Cat) - Unterklasse von Felidae

  /\_/\
 ( o.o )
  > ^ <

class Katze(Felidae):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, schnurrhaare_laenge):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe, True) # Katzen sind oft nachtaktiv
        self.schnurrhaare_laenge = schnurrhaare_laenge

    def miauen(self):
        return f"{self.name} miaut leise: Miau!"

    def klettern(self):
        return f"{self.name} klettert auf einen Baum."

---

# Tiger (Tiger) - Unterklasse von Felidae (Einzelgänger)

   /\_/\
  / o o \
 (   ^   )
  \_ U _/
    \_|_/

class Tiger(Felidae):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, streifenmuster):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe, True) # Tiger sind nachtaktiv
        self.streifenmuster = streifenmuster

    def jagen(self, beute):
        return f"{self.name} lauert auf {beute} und greift an."

---

# Löwe (Lion) - Unterklasse von Felidae (Rudel, soziale Tiere)

   /\_/\
  / o o \
 (   ^   )
  \_ U _/
    \_|_/
   (___)

class Löwe(Felidae):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, mähne_groesse):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe, False) # Löwen sind tagaktiver als andere Katzen
        self.mähne_groesse = mähne_groesse

    def brüllen(self):
        return f"{self.name} brüllt majestätisch."

    def rudel_jagd(self, beute):
        return f"{self.name} beteiligt sich an der Jagd auf {beute} mit dem Rudel."

---

# Bär (Bear) - Unterklasse von Säugetier (Bleibt direkt unter Säugetier, da keine spezifische Unterfamilie für dieses Beispiel)

    .--.
   /    \
  |o_o |
  |:_/ |
 //   \ \
(|     | )
/'\_   _/`\
\___)=(___/

class Bär(Säugetier):
    def __init__(self, name, alter, geschlecht, gewicht, fellfarbe, winterschlaf_bereit):
        super().__init__(name, alter, geschlecht, gewicht, fellfarbe)
        self.winterschlaf_bereit = winterschlaf_bereit

    def brüllen(self):
        return f"{self.name} brüllt furchterregend."

    def angeln(self):
        return f"{self.name} angelt nach Lachsen."

---

## Beispiele zur Nutzung der Klassen

```python
# Instanzen erstellen
fido = Hund("Fido", 7, "männlich", 30, "braun", "Labrador")
mittens = Katze("Mittens", 4, "weiblich", 5, "grau", "lang")
grauwolf = Wolf("Grauwolf", 6, "männlich", 45, "grau", "Schattenrudel")
balu = Bär("Balu", 12, "männlich", 300, "braun", True)
sher_khan = Tiger("Sher Khan", 8, "männlich", 220, "orange-schwarz", "ausgeprägt")
simba = Löwe("Simba", 9, "männlich", 190, "golden", "groß")

# Methoden aufrufen
print(fido.vorstellen())
print(fido.fressen("Trockenfutter"))
print(fido.bellen())
print(fido.apportieren("Ball"))
print(fido.altern())
print(fido.kommunizieren()) # Methode von Canidae
print("-" * 30)

print(mittens.vorstellen())
print(mittens.trinken())
print(mittens.miauen())
print(mittens.klettern())
print(mittens.schleichen()) # Methode von Felidae
print("-" * 30)

print(grauwolf.vorstellen())
print(grauwolf.heulen())
print(grauwolf.jagen("Hirsch"))
print(grauwolf.spuren_lesen()) # Methode von Canidae
print("-" * 30)

print(balu.vorstellen())
print(balu.brüllen())
print(balu.angeln())
print("-" * 30)

print(sher_khan.vorstellen())
print(sher_khan.schleichen()) # Methode von Felidae
print(sher_khan.jagen("Zebra"))
print(sher_khan.lauern("Antilope")) # Methode von Felidae
print("-" * 30)

print(simba.vorstellen())
print(simba.brüllen())
print(simba.rudel_jagd("Büffel"))
print(simba.schleichen()) # Methode von Felidae

